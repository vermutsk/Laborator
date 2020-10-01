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
test = 0
new_collection = db[f'{test}']
new_collection.drop()
#coll = db.collection_names()
#coll.reverse()
#if len(coll) != 0:
#    test = coll[0]
#    test = int(test)
new_collection = db[f'{test}']
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
        self.ui.OpenBox.currentIndexChanged.connect(self.openButt)
        self.ui.AnalizButt.clicked.connect(self.analizButt)
        self.ui.change_cbButt.clicked.connect(self.search_with_param)
        self.ui.saveButt.clicked.connect(self.save_Data)
        self.ui.DeleteButt.clicked.connect(self.delete_data)
        self.my_pool = mp.Pool(1)
        self.callback_obj = SyncObj()
        self.callback_obj.progressBarUpdated.connect(self.ui.progressBar.setValue)
        self.callback_obj.progressBarUpdated_2.connect(self.ui.progressBar_2.setValue)
        self.callback_obj.tableUpdatedRow.connect(self.UpdateTableRow)
        self.callback_obj.tableUpdatedHeader.connect(self.UpdateTableHeader)

    def locker(self):
        self.ui.AnalizButt.setDisabled(True)
        self.ui.saveButt.setDisabled(True)
        self.ui.change_cbButt.setDisabled(True)
        self.ui.DeleteButt.setDisabled(True)

    def unlocker(self):
        self.ui.AnalizButt.setDisabled(False)
        self.ui.saveButt.setDisabled(False)
        self.ui.change_cbButt.setDisabled(False)
        self.ui.DeleteButt.setDisabled(False)

    #Delete
    def delete_data(self):
        row = self.ui.tableWidget.currentIndex().row()
        data = []
        res = []
        row1 = {}
        for i in range(7):
            item = self.ui.tableWidget.item(row, i).text()
            data.append(item)
        header= ['number', 'name', 'fname', 'phone', 'uid', 'nik', 'wo']
        for i in range(7):
            row2 = {}
            row2 = {header[i] : data[i]}
            row1.update(row2)
        res.append(row1)
        print(res)
        new_collection.delete_one(row1)

    #Update
    #Save
    def save_Data(self):
        self.locker()
        header = ['№', 'name', 'fname', 'phone', 'uid', 'nik', 'wo']
        rowCount = self.ui.tableWidget.rowCount()
        columCount = 7
        d = QFileDialog.getSaveFileName(self, "Сохранение", "/analized_table",
                                                "Файл Microsoft Excel (*.csv)")
        if d[0] == '':
            QMessageBox.about(self, 'Ошибка', 'Вы отменили сохранение')
            self.unlocker()
            return 1
        value = 0
        step = 100/rowCount
        with open(d[0], 'w', newline='') as file_csv:
            writher = csv.writer(file_csv, delimiter = '|')
            writher.writerow(header)
            for i in range(rowCount):
                save = []
                value += step
                self.callback_obj.progressBarUpdated.emit(value)
                for j in range(columCount):
                    p = self.ui.tableWidget.item(i, j).text()
                    save.append(p)
                writher.writerow(save)
        self.callback_obj.progressBarUpdated.emit(0)
        self.unlocker()

    #Open
    def openButt(self):
        id = self.ui.OpenBox.currentIndex()
        if id == 1:
            fileD = QFileDialog()
            open_file = fileD.getExistingDirectory(self)
            self.ui.PathFile.setText('')
            self.ui.PathFile.setText(open_file)
        elif id ==2:
            str0, ok = QInputDialog.getText(self, "Ввод параметра", "Введите данные в виде: name|fname|phone|uid|nik|wo", QLineEdit.Normal,'')
            if str0 and ok:
                data = str0.split('|')
                if len(data) == 6:
                    res = []
                    row = {}
                    pers_id, number = self.check_last_doc()
                    data.reverse()
                    data.append(f'{number + 1}')
                    data.append(f'{pers_id + 1}')
                    data.reverse()
                    header= ['pers_id','number', 'name', 'fname', 'phone', 'uid', 'nik', 'wo']
                    for i in range(8): 
                        row1 = {}
                        row1 = {header[i] : data[i]}
                        row.update(row1)
                    res.append(row)
                    new_collection.insert_many(res)
                    print(res)
                    if number + 1 <= 100:
                        data.pop(0)
                        self.callback_obj.tableUpdatedRow.emit(pers_id, 0, data)
                    else:
                        pass
                    self.chek = True
                else:
                    QMessageBox.about(self, 'Ошибка', 'Неверный формат данных')
                    self.unlocker()
                print(data)
                lenght = new_collection.find().count()
                print(lenght)
            else:
                QMessageBox.about(self, 'Ошибка', 'Введите данные.')
                self.unlocker()


    #Загрузка в таблицу + сортировка
    def UpdateTableRow(self, i, miim, row):
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
        for j, v in enumerate(row):
            it = QTableWidgetItem()
            it.setData(Qt.DisplayRole, v)
            self.ui.tableWidget.setItem((i - miim), j, it)
            print(i-miim, j)

    def UpdateTableHeader(self, row):
        self.ui.tableWidget.setHorizontalHeaderLabels(row)


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
        pers_id, number = self.check_last_doc()
        self.my_pool.apply_async(func=read_dir, args=(csv_files, pers_id), callback=self.set_data)


    def import_data(self, miim, maam):
        value = 0
        head = self.serch('number','№')
        self.UpdateTableHeader(head)
        self.ui.tableWidget.setRowCount(0)
        for i in range(miim, maam + 1):
            solo_data = self.serch('pers_id', f'{i}')
            value += 1
            self.callback_obj.progressBarUpdated.emit(value)
            self.callback_obj.tableUpdatedRow.emit(i, miim, solo_data)
        print(i, miim, maam)
        self.callback_obj.progressBarUpdated.emit(value + 1)
        self.callback_obj.progressBarUpdated.emit(0)

    def serch(self, param, value):
        print('я пытался')
        js = new_collection.find({param : value}, { '_id' : 0, 'pers_id' : 0})
        many_doc = []
        one_doc = []
        for doc in js:
            one_doc = []
            for value in doc.values():
                one_doc.append(value)
            many_doc.append(one_doc)
        if len(many_doc) > 1:
            return many_doc
        else:
            return one_doc

    def search_with_param(self):
        if self.chek:
            id = self.ui.comboBox.currentIndex()
            value, ok = QInputDialog.getText(self, "Ввод параметра", "Введите параметр для поиска:", QLineEdit.Normal,'')
            if ok and value:
                if id ==1:
                    print(value)
                    one_doc = self.serch('nik', value)
                    print(one_doc)
                elif id == 2:
                    one_doc = self.serch('phone', value)
                elif id == 3:
                    one_doc = self.serch('fname', value)
                if len(one_doc) != 0:
                    self.ui.tableWidget.setRowCount(0)
                    row_count = len(one_doc)
                    value = 0
                    if type(one_doc[0]) == list:
                        for i in range(row_count):
                            solo_data = one_doc[i]
                            value += 1
                            self.callback_obj.progressBarUpdated.emit(value)
                            self.callback_obj.tableUpdatedRow.emit(i, 0, solo_data)
                    else:
                        solo_data = one_doc
                        value += 1
                        self.callback_obj.progressBarUpdated.emit(value)
                        self.callback_obj.tableUpdatedRow.emit(0, 0, solo_data)
                    self.callback_obj.progressBarUpdated.emit(value + 1)
                    self.callback_obj.progressBarUpdated.emit(0)
                    
                else:
                    QMessageBox.about(self, 'Ошибка', 'Параметр не найден')
                    self.unlocker()
            else:
                QMessageBox.about(self, 'Ошибка', 'Введите параметр.')
                self.unlocker()
        else:
            QMessageBox.about(self, 'Ошибка', 'Проанализируйте файл.')
            self.unlocker()

    def change_size(self):
        miim = 1
        maam = 100
        if self.chek:
            miim_maam0 = self.ui.comboBox_2.currentText()
            miim_maam = miim_maam0.split(' - ')
            miim = int(miim_maam[0])
            maam = int(miim_maam[1])
        return miim, maam

    def change_size_butt(self):
        miim, maam = self.change_size()
        self.import_data(miim, maam)

    def set_data(self, lenght):
        miim, maam = self.change_size()
        count_box = self.ui.comboBox_2.count()
        ost = lenght % 100
        count_id = lenght - ost
        count_id = int(count_id / 100)
        self.import_data(miim, maam)
        if count_box > 1:
            self.ui.comboBox_2.clear()
            self.ui.comboBox_2.addItem("1 - 100")
            self.ui.comboBox_2.setCurrentIndex(0)
        for i in range(1, count_id):
            self.ui.comboBox_2.addItem(f"{i}01 - {i+1}00")
        ost += count_id * 100
        self.ui.comboBox_2.addItem(f"{count_id * 100} - {ost}")
        self.unlocker()
        self.chek = True

    def check_last_doc(self):
        pers_id = 0
        number = 0
        if self.chek:
            last_doc = new_collection.find().sort('_id', -1).limit(1)
            for doc in last_doc:
                one_doc = []
                for value in doc.values():
                    one_doc.append(value)
                one_doc.pop(0) 
                pers_id = one_doc[0]
                number = one_doc[1]
        print(pers_id, number)
        return int(pers_id), int(number)


def read_dir(csv_files, pers_id):
    for i in range(len(csv_files)):
        with open(csv_files[i], 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter = '|')
            header= ['pers_id', 'number', 'name', 'fname', 'phone', 'uid', 'nik', 'wo']
            res = []
            for each in reader:
                row = {}
                trash = each.count('')
                for i in range(trash):
                    each.remove('')
                each.reverse()
                each.append(f'{pers_id}')
                each.reverse()
                pers_id += 1
                for i in range(8):
                    row2 = {}
                    row2 = {header[i] : each[i]}
                    row.update(row2)
                print(each)
                res.append(row)
            new_collection.insert_many(res)
    lenght = new_collection.find().count()
    return lenght


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Win()
    w.show()
    sys.exit(app.exec_())