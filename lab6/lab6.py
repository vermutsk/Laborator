import os
import sys
import csv
import datetime
import multiprocessing as mp
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject, Signal,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import (QScrollArea, QWidget, QTableView, QPushButton,
    QProgressBar, QComboBox, QApplication, QMainWindow, QAbstractItemView, 
    QMessageBox, QTableWidgetItem, QFileDialog, QInputDialog, QLineEdit)
from widget import Ui_MainWindow

class SyncObj(QObject):
    progressBarUpdated = Signal(int)
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
        #self.ui.serchData.clicked.connect(self.serch_Data)
        self.ui.saveButt.clicked.connect(self.save_Data)
        self.my_pool = mp.Pool(1)
        self.callback_obj = SyncObj()
        self.callback_obj.progressBarUpdated.connect(self.ui.progressBar.setValue)
        self.callback_obj.tableUpdatedRow.connect(self.UpdateTableRow)
        self.callback_obj.tableUpdatedHeader.connect(self.UpdateTableHeader)

    def openButt(self):
        fileD = QFileDialog()
        open_file = fileD.getExistingDirectory(self)
        self.ui.PathFile.setText('')
        self.ui.PathFile.setText(open_file)

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

    def set_data(self, solo_data):
        if self.data_array != []:
            self.data_array.clear()
        if self.data_array != []:
            self.login_array.clear()
        miim = 0
        maam = 99
        print(self.data_array)

        self.UpdateTableHeader(solo_data[0])
        value = 0
        self.ui.tableWidget.setRowCount(0)
        for i, row in enumerate(solo_data[1:]):
            value += 1
            self.callback_obj.progressBarUpdated.emit(value)
            if miim <= i <= maam:
                self.callback_obj.tableUpdatedRow.emit(i, miim, row)


        self.callback_obj.progressBarUpdated.emit(value + 1)
        self.callback_obj.progressBarUpdated.emit(0)
        self.save_array = list.copy(solo_data)
        self.unlocker()
        self.chek = True

    def change_cb_index(self):
        id = self.ui.comboBox.currentIndex()
        print(id)
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
                    self.ui.tableWidget.setRowCount(0)
                    self.UpdateTableHeader(self.save_array[0])
                    p = 0
                    value = 0
                    for i, row in enumerate(self.save_array[1:]):
                        value += 1
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
                    self.callback_obj.progressBarUpdated.emit(value + 1)
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
            d_t, ok = QInputDialog.getText(self, "Ввод даты и времени", "Введите дату и время для поиска:\nФормат YYYY.MM.DD HH:MM:SS", QLineEdit.Normal,'')
            if ok and d_t:
                d_t = d_t.split(' ')
                age = d_t[0]
                clock = d_t[1]
                age = age.split('.')
                clock = clock.split(':')
                unix_time = datetime.datetime(int(age[2]), int(age[1]), int(age[0]), int(clock[0]), int(clock[1]),
                                              int(clock[2])).timestamp()
                unix_time = int(unix_time)
                unix_time += (36000)
                unix_time = str(unix_time)
                if unix_time in self.data_array:
                    self.data_array.clear()
                    self.ui.tableWidget.setRowCount(0)
                    self.UpdateTableHeader(self.save_array[0])
                    p = 0
                    value = 0
                    for i, row in enumerate(self.save_array[1:]):
                        value += 1
                        self.callback_obj.progressBarUpdated.emit(value)
                        if unix_time == row[0]:
                            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                            for j, v in enumerate(row):
                                if j == 3:
                                    self.login_array.append(v)
                                it = QTableWidgetItem()
                                it.setData(Qt.DisplayRole, v)
                                self.ui.tableWidget.setItem(p, j, it)
                            p += 1
                    self.callback_obj.progressBarUpdated.emit(value + 1)
                    self.callback_obj.progressBarUpdated.emit(0)
                    self.unlocker()
                    pass
                else:
                    QMessageBox.about(self, 'Ошибка', 'Дата и время не найдены')
                    self.unlocker()
            else:
                QMessageBox.about(self, 'Ошибка', 'Введите дату и время')
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
        with open(d[0], 'w', newline='') as file_csv:
            writher = csv.writer(file_csv)
            writher.writerow(header)
            for i in range(rowCount):
                save = []
                value += 1
                self.callback_obj.progressBarUpdated.emit(value)
                for j in range(columCount):
                    p = self.ui.tableWidget.item(i, j).text()
                    save.append(p)
                writher.writerow(save)
        self.callback_obj.progressBarUpdated.emit(value + 1)
        self.callback_obj.progressBarUpdated.emit(0)
        self.unlocker()

    def analizButt(self):
        self.locker()
        path_file = self.ui.PathFile.text()
        if os.path.exists(path_file) is False:
            QMessageBox.about(self, 'Ошибка', 'Введите путь')
            self.ui.PathFile.setText('')
            self.unlocker()
            return 2
        list_dir = os.listdir(path_file)
        csv_files = []
        for i in range(len(list_dir)):
            get_path = os.path.join(path_file, list_dir[i])
            chek = os.path.isfile(get_path)
            if chek:
                sp_file = list_dir[i].split('.')
                if sp_file[-1] == 'csv':
                    csv_files.append(get_path)

        if len(csv_files) == 0:
            QMessageBox.about(self, 'Ошибка', 'Не найденны csv файлы')
            self.unlocker()
        self.my_pool.apply_async(func=read_ddir, args=(csv_files,), callback=self.set_data)

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


def read_ddir(csv_files):
    all_data = []
    for i in range(len(csv_files)):
        with open(csv_files[i], 'r')as csv_file:
            reader = csv.reader(csv_file)  # reader - список списков
            data = list(reader)
        all_data.append(data)
    solo_data = list.copy(all_data[0])
    for i in range(1, len(all_data)):
        all_data[i].remove(all_data[i][0])
        solo_data += all_data[i]
    return solo_data

#class TadleWidgetWindow(object):
#    def setapUi(self, MainWindow):
#        MainWindow.setObjectName("MainWindow")
#        MainWindow.resize(600, 600)
#        self.centralWidget = QWidget(MainWindow)
#        self.centralWidget.resize(500, 500)
#        vbox = QVBoxLayout(self.centralWidget)
#        self.TabletWidget = QTableWidget()
#        vbox.addWidget(self.TabletWidget)
#        self.TabletWidget.setColumnCount(17)
#        list1 = ['1', '2', '3', '4']
#        l = [i for i in range(len(list1))]#Длина списка
#        self.TabletWidget.setRowCount(l) 
#        self.column_label = ['begin', 'end', 'time interval', 'login', 'mac ab','ULSK1',\
#                            'BRAS ip', ', start count', 'alive count', 'stop count', \
#                            'incoming', 'outcoming', 'error_count','code 0', 'code 1011',\
#                             'code 1100', 'code -3', 'code -52', 'code -42', 'code -21', \
#                             ', code -40', 'code -44', 'code -46', 'code -38']
#        self.row_label = l
#        self.TabletWidget.HorizontalHeaderLadels(self.column_label)
#        self.TabletWidget.VerticalHeaderLadels(self.row_label)
#        self.TabletWidget.setSortingEnabled(True)
#
#class MainWindow(QMainWindow, TadleWidgetWindow):
#    def __init__(self, parent=None, *args, **kwargs):
#        QMainWindow.__init__(self)
#        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Win()
    w.show()
    sys.exit(app.exec_())



