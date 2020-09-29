import os
import sys
import csv
import datetime
import multiprocessing as mp
from pymongo import MongoClient
from widget import Ui_MainWindow
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject, Signal,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import (QScrollArea, QWidget, QTableView, QPushButton,
    QProgressBar, QComboBox, QApplication, QMainWindow, QAbstractItemView, 
    QMessageBox, QTableWidgetItem, QFileDialog, QInputDialog, QLineEdit)

client = MongoClient("localhost", 27017) 
db = client['NEW_DB']
new_collection = db['new']
new_collection.drop()
new_collection = db['new']
lenght = new_collection.find().count()


class SyncObj(QObject):
    progressBarUpdated = Signal(int)
    progressBarUpdated_2 = Signal(int)
    tableUpdatedRow = Signal((int, int, list))
    tableUpdatedHeader = Signal(int)

class Win(QMainWindow):
    def __init__(self, parent=None):
        super(Win, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.chek = False
        self.ui.comboBox_2.currentIndexChanged.connect(self.change_size_butt)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.PathFile.setReadOnly(True)
        self.ui.OpenButt.clicked.connect(self.openButt)
        self.ui.AnalizButt.clicked.connect(self.analizButt)
        self.ui.change_cbButt.clicked.connect(self.change_cb_index)
        #self.ui.saveButt.clicked.connect(self.save_Data)
        self.my_pool = mp.Pool(1)
        self.callback_obj = SyncObj()
        self.callback_obj.progressBarUpdated.connect(self.ui.progressBar.setValue)
        self.callback_obj.progressBarUpdated_2.connect(self.ui.progressBar_2.setValue)
        self.callback_obj.tableUpdatedRow.connect(self.UpdateTableRow)
        self.callback_obj.tableUpdatedHeader.connect(self.UpdateTableHeader)

    def UpdateTableRow(self, i, miim, row):
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
        for j, v in enumerate(row):
            it = QTableWidgetItem()
            it.setData(Qt.DisplayRole, v)
            self.ui.tableWidget.setItem((i - miim), j, it)

    def UpdateTableHeader(self, row):
        self.ui.tableWidget.setHorizontalHeaderLabels(row)

    def openButt(self):
        fileD = QFileDialog()
        open_file = fileD.getExistingDirectory(self)
        self.ui.PathFile.setText('')
        self.ui.PathFile.setText(open_file)

    def analizButt(self):
        self.locker()
        way_file = self.ui.PathFile.text()
        if os.path.exists(way_file) is False:
            QMessageBox.about(self, 'Ошибка', 'Введите путь')
            self.ui.PathFile.setText('')
            self.unlocker()
            return 2
        list_dir = os.listdir(way_file)
        csv_files = []
        for i in range(len(list_dir)):
            get_path = os.path.join(way_file, list_dir[i])
            chek = os.path.isfile(get_path)
            if chek:
                sp_file = list_dir[i].split('.')
                if sp_file[-1] == 'txt':
                    csv_files.append(get_path)

        if len(csv_files) == 0:
            QMessageBox.about(self, 'Ошибка', 'Не найденны txt файлы')
            self.unlocker()
        self.my_pool.apply_async(func=read_dir, args=(csv_files,), callback=self.set_data)


    def change_cb_index(self):
        if self.chek:
            id = self.ui.comboBox.currentIndex()
            value, ok = QInputDialog.getText(self, "Ввод параметра", "Введите параметр для поиска:", QLineEdit.Normal,'')
            if ok and value:
                if id ==1:
                    one_doc = self.serch('nik', value)
                elif id == 2:
                    one_doc = self.serch('phone', value)
                elif id == 3:
                    one_doc = self.serch('fname', value)
                if len(one_doc) != 0:
                    value = 0
                    if all(isinstance(i, list) for i in one_doc):
                        for i in range(len(one_doc)):
                            solo_data = one_doc[i]
                            print(one_doc, solo_data)
                            value += 1
                            self.callback_obj.progressBarUpdated.emit(value)
                            self.callback_obj.tableUpdatedRow.emit(i, 0, solo_data)
                        #выводит первые сто......................................................
                    else:
                        solo_data = one_doc
                        print(one_doc, solo_data)
                        value += 1
                        self.callback_obj.progressBarUpdated.emit(value)
                        self.callback_obj.tableUpdatedRow.emit(0, 0, solo_data)
                    self.callback_obj.progressBarUpdated.emit(value + 1)
                    self.callback_obj.progressBarUpdated.emit(0)
                    #выводит в первую строку нужное значение + заполняет остальные лишними значениями..
                else:
                    QMessageBox.about(self, 'Ошибка', 'Параметр не найден')
                    self.unlocker()
            else:
                QMessageBox.about(self, 'Ошибка', 'Введите параметр.')
                self.unlocker()
        else:
            QMessageBox.about(self, 'Ошибка', 'Проанализируйте файл.')
            self.unlocker()

    def serch(self, param, value):
        js = new_collection.find({param : value}, { '_id' : 0 })
        one_doc = []
        for doc in js:
            for value in doc.values():
                one_doc.append(value)
        return one_doc

    def change_size(self):
        miim = 1
        maam = 100
        if self.chek:
            miim_maam0 = self.ui.comboBox_2.currentText()
            miim_maam = miim_maam0.split(' - ')
            miim = int(miim_maam[0])
            maam = int(miim_maam[1])
        return miim, maam

    def import_data(self, miim, maam):
        value = 0
        head = self.serch('number','№')
        self.UpdateTableHeader(head)
        self.ui.tableWidget.setRowCount(0)
        for i in range(miim, maam + 1):
            solo_data = self.serch('number', f'{i}')
            value += 1
            self.callback_obj.progressBarUpdated.emit(value)
            self.callback_obj.tableUpdatedRow.emit(i, miim, solo_data)
        self.callback_obj.progressBarUpdated.emit(value + 1)
        self.callback_obj.progressBarUpdated.emit(0)

    def change_size_butt(self):
        miim, maam = self.change_size()
        self.import_data(miim, maam)

    def set_data(self, lenght):
        miim, maam = self.change_size()
        id = self.ui.comboBox_2.currentIndex()
        count_box = self.ui.comboBox_2.count()
        for i in range(count_box):
            if id == i:
                miim = i * 100 + 1
                maam = (i + 1) * 100
        ost = lenght % 100
        count_id = lenght - ost
        count_id = int(count_id / 100)

        self.import_data(miim, maam)

        if count_box > 1:
            self.ui.comboBox_2.clear()
            self.ui.comboBox_2.addItem("1 - 100")
            self.ui.comboBox_2.setCurrentIndex(0)
        for i in range(1, count_id):
            self.ui.comboBox_2.addItem(f"{i}00 - {i+1}00")
        ost += count_id * 100
        self.ui.comboBox_2.addItem(f"{count_id * 100} - {ost}")
        
        #self.save_array = list.copy(solo_data)
        self.unlocker()
        self.chek = True

    def locker(self):
        self.ui.AnalizButt.setDisabled(True)
        self.ui.saveButt.setDisabled(True)
        self.ui.change_cbButt.setDisabled(True)
        self.ui.OpenButt.setDisabled(True)


    def unlocker(self):
        self.ui.AnalizButt.setDisabled(False)
        self.ui.saveButt.setDisabled(False)
        self.ui.change_cbButt.setDisabled(False)
        self.ui.OpenButt.setDisabled(False)


def read_dir(csv_files):
    for i in range(len(csv_files)):
        with open(csv_files[i], 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter = '|')
            header= ['number', 'name', 'fname', 'phone', 'uid', 'nik', 'wo']
            res = []
            for each in reader:
                row = {}
                trash = each.count('')
                for i in range(trash):
                    each.remove('')
                for i in range(7):
                    row2 = {}
                    row2 = {header[i] : each[i]}
                    row.update(row2)
                res.append(row)
            new_collection.insert_many(res)
    lenght = new_collection.find().count()
    return lenght


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Win()
    w.show()
    sys.exit(app.exec_())