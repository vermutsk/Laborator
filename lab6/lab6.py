import os
import sys
import csv
import datetime
import multiprocessing as mp
from widget import Ui_MainWindow
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject, Signal,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import (QScrollArea, QWidget, QTableView, QPushButton,
    QProgressBar, QComboBox, QApplication, QMainWindow, QAbstractItemView, 
    QMessageBox, QTableWidgetItem, QFileDialog, QInputDialog, QLineEdit)

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
        self.login_array = []
        self.data_array = []
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.PathFile.setReadOnly(True)
        self.ui.OpenButt.clicked.connect(self.openButt)
        self.ui.AnalizButt.clicked.connect(self.analizButt)
        self.ui.change_cbButt.clicked.connect(self.change_cb_index)
        self.ui.change_sizeButt.clicked.connect(self.change_size)
        self.ui.saveButt.clicked.connect(self.save_Data)
        self.my_pool = mp.Pool(1)
        self.callback_obj = SyncObj()
        self.callback_obj.progressBarUpdated.connect(self.ui.progressBar.setValue)
        self.callback_obj.progressBarUpdated_2.connect(self.ui.progressBar_2.setValue)
        self.callback_obj.tableUpdatedRow.connect(self.UpdateTableRow)
        self.callback_obj.tableUpdatedHeader.connect(self.UpdateTableHeader)

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
                if sp_file[-1] == 'csv':
                    csv_files.append(get_path)

        if len(csv_files) == 0:
            QMessageBox.about(self, 'Ошибка', 'Не найденны csv файлы')
            self.unlocker()
        self.my_pool.apply_async(func=read_dir, args=(csv_files,), callback=self.set_data)
   
    def set_data(self, solo_data):
        self.locker()
        if self.data_array != []:
            self.data_array.clear()
        if self.data_array != []:
            self.login_array.clear()
        miim, maam = self.change_size()
        value = 0
        value1 = 0
        step = 100/maam
        if len(solo_data) >= maam:  
            step1 = 100/(len(solo_data)-maam)
        self.ui.tableWidget.setRowCount(0)
        for i, row in enumerate(solo_data[1:]):
            value += step
            self.callback_obj.progressBarUpdated.emit(value)
            if miim <= i <= maam:
                self.callback_obj.tableUpdatedRow.emit(i, miim, row)
            if i >= maam:
                value1 += step1
                self.callback_obj.progressBarUpdated_2.emit(value1)
        self.callback_obj.progressBarUpdated.emit(0)
        self.callback_obj.progressBarUpdated_2.emit(0)
        self.save_array = list.copy(solo_data)
        self.unlocker()
        self.chek = True
    
    def change_size(self):
        miim = 0
        maam = 999
        if self.chek:
            size = self.ui.change_sizeLine.text()
            if size == '':
                miim = 0
                maam = 999
                self.ui.change_sizeLine.setToolTip('')
            elif len(size)>2 and size.find('-') != -1 and size.count('-')==1:
                size = size.split('-')
                miim0 = size[0]
                maam0 = size[1]
                try:
                    if int(miim0)<int(maam0) and int(miim0)>=0:
                        if int(maam0) - int(miim0) <= 10000 or int(maam0)<11000:
                            if int(miim0)>0:
                                self.ui.change_sizeLine.setToolTip('')
                                miim = int(miim0)-1
                                maam = int(maam0)-1
                            elif int(miim0)==0:
                                self.ui.change_sizeLine.setToolTip('')
                                miim = int(miim0)
                                maam = int(maam0)
                        else:
                            self.ui.change_sizeLine.setToolTip('Ошибка: слишком большой интервал')
                            QMessageBox.about(self, 'Ошибка', 'Cлишком большой интервал')
                    else:
                        self.ui.change_sizeLine.setToolTip('Ошибка: min > max')
                        QMessageBox.about(self, 'Ошибка', 'min > max')
                except Exception:
                    self.ui.change_sizeLine.setToolTip('Ошибка: введите численные значения')
                    QMessageBox.about(self, 'Ошибка', 'Введите численные значения')   
            else:
                self.ui.change_sizeLine.setToolTip('Ошибка: введите в виде "int-int"')
                QMessageBox.about(self, 'Ошибка', 'Введите в виде "int-int"')
        return miim, maam

    def UpdateTableRow(self, i, miim, row):
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
        for j, v in enumerate(row):
            if j == 0:
                self.data_array.append(v)
            elif j == 3:
                self.login_array.append(v)
            it = QTableWidgetItem()
            it.setData(Qt.DisplayRole, v)
            self.ui.tableWidget.setItem((i - miim), j, it)

    def UpdateTableHeader(self, row):
        self.ui.tableWidget.setHorizontalHeaderLabels(row)

    def change_cb_index(self):
        id = self.ui.comboBox.currentIndex()
        if id ==1:
            self.serch_Login()
        elif id == 2:
            self.serch_Data()

    def serch_Login(self):
        self.locker()
        if self.data_array != []:
            self.data_array.clear()
        if self.chek:
            login, ok = QInputDialog.getText(self, "Ввод логина", "Введите логин для поиска:", QLineEdit.Normal,'')
            if ok and login:
                if login in self.login_array:
                    self.login_array.clear()
                    p = 0
                    value = 0
                    max = len(self.save_array[1:])
                    step = 100/max
                    for row in self.save_array[1:]:
                        value += step
                        self.callback_obj.progressBarUpdated.emit(value)
                        if login in row:
                            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                            for j, v in enumerate(row):
                                if j == 0:
                                    self.data_array.append(v)
                                it = QTableWidgetItem()
                                it.setData(Qt.DisplayRole, v)
                                self.ui.tableWidget.setItem(p, j, it)
                            p += 1
                    self.callback_obj.progressBarUpdated.emit(0)
                    self.unlocker()
                else:
                    QMessageBox.about(self, 'Ошибка', 'Логина не найдено.')
                    self.unlocker()
            else:
                QMessageBox.about(self, 'Ошибка', 'Введите логин.')
                self.unlocker()
        else:
            QMessageBox.about(self, 'Ошибка', 'Проанализируйте файл.')
            self.unlocker()
        
    def serch_Data(self):
        self.locker()
        if self.login_array != []:
            self.login_array.clear()
        if self.chek:
            enter = self.ui.dateTimeEdit.text()
            enter = enter.split(' ')
            age = enter[0]
            clock = enter[1]
            age = age.split('.')
            clock = clock.split(':')
            unix_time = datetime.datetime(int(age[2]), int(age[1]), int(age[0]), int(clock[0]), int(clock[1]),
                                          int(clock[2])).timestamp()
            unix_time = int(unix_time)
            unix_time = str(unix_time)
            if unix_time in self.data_array:
                self.data_array.clear()
                self.ui.tableWidget.setRowCount(0)
                self.UpdateTableHeader(self.save_array[0])
                p = 0
                value = 0
                max = len(self.save_array[1:])
                step = 100/max
                for row in self.save_array[1:]:
                    value += step
                    self.callback_obj.progressBarUpdated.emit(value)
                    if row[0] <= unix_time <= row[1]:
                        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                        for j, v in enumerate(row):
                            if j == 3:
                                self.login_array.append(v)
                            it = QTableWidgetItem()
                            it.setData(Qt.DisplayRole, v)
                            self.ui.tableWidget.setItem(p, j, it)
                        p += 1
                self.callback_obj.progressBarUpdated.emit(0)
                self.unlocker()
                pass
            else:
                QMessageBox.about(self, 'Ошибка', 'Дата не найдена')
                self.unlocker()
        else:
            QMessageBox.about(self, 'Ошибка', 'Проанализируйте файл')
            self.unlocker()

    def save_Data(self):
        self.locker()
        header = ['begin', 'end', 'time interval', 'login', 'mac ab', 'ULSK1', 'BRAS ip', 'start count', 'alive count',
                  'stop count', 'incoming', 'outcoming', 'error_count', 'code 0', 'code 1011', 'code 1100', 'code -3',
                  'code -52', 'code -42', 'code -21', 'code -40', ' code -44', 'code -46', ' code -38']
        rowCount = self.ui.tableWidget.rowCount()
        columCount = 24
        d = QFileDialog.getSaveFileName(self, "Сохранение", "/analized_table",
                                                  "Файл Microsoft Excel (*.csv)")
        if d[0] == '':
            QMessageBox.about(self, 'Ошибка', 'Вы отменили сохранение')
            self.unlocker()
            return 1
        value = 0
        step = 100/rowCount
        with open(d[0], 'w', newline='') as file_csv:
            writher = csv.writer(file_csv)
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

    def locker(self):
        self.ui.AnalizButt.setDisabled(True)
        self.ui.saveButt.setDisabled(True)
        self.ui.change_cbButt.setDisabled(True)
        self.ui.OpenButt.setDisabled(True)
        self.ui.change_sizeButt.setDisabled(True)
        self.ui.change_sizeLine.setDisabled(True)

    def unlocker(self):
        self.ui.AnalizButt.setDisabled(False)
        self.ui.saveButt.setDisabled(False)
        self.ui.change_cbButt.setDisabled(False)
        self.ui.OpenButt.setDisabled(False)
        self.ui.change_sizeButt.setDisabled(False)
        self.ui.change_sizeLine.setDisabled(False)


def read_dir(csv_files):
    files = []
    for i in range(len(csv_files)):
        with open(csv_files[i], 'r') as csv_file:
            reader = csv.reader(csv_file)
            data = list(reader)
        files.append(data)
    solo_data = list.copy(files[0])
    for i in range(1, len(files)):
        files[i].remove(files[i][0])
        solo_data += files[i]
    return solo_data


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Win()
    w.show()
    sys.exit(app.exec_())



