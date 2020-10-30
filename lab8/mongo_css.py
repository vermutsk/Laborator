import os
import sys
import csv
from pymongo import MongoClient
from widget import Ui_MainWindow
from PySide2.QtCore import (Signal, QObject, Qt)
from PySide2.QtGui import (QCursor)
from PySide2.QtWidgets import (QScrollArea, QPushButton, QProgressBar, QComboBox, QApplication, QMainWindow, 
    QAbstractItemView, QMessageBox, QTableWidgetItem, QFileDialog, QInputDialog, QLineEdit, QProgressDialog)

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

class Worker(QObject):
    loaded = Signal(int, str)
    finished = Signal()
    def __init__(self, csv_files, b):
        super().__init__()
        self._files = csv_files
        self._size = b

    def run(self):
        self._stop = False
        step = 0
        for i in range(len(self._files)):   
            with open(self._files[i], 'r') as csv_file:
                size0 = 0
                for k in range(100):
                    line = csv_file.readline()
                    size0 += sys.getsizeof(line)
                lenght = size0 / 100
                lenght = int(self._size / lenght)
                self.showProgress('Загрузка файлов', lenght, self.stop)
                self.loaded.connect(self.updateProgress) 
                csv_file.seek(0)
                reader = csv.reader(csv_file, delimiter = '|')
                header = ['number', 'name', 'fname', 'phone', 'uid', 'nik', 'wo']
                num = 0
                res = []
                for each in reader:
                    num += 1
                    if self._stop:
                        break
                    row = {}
                    trash = each.count('')
                    for i in range(trash):
                        each.remove('')
                    try:
                        for i in range(7):
                            row2 = {}
                            row2 = {header[i] : each[i]}
                            row.update(row2)
                    except IndexError:
                        pass
                    res.append(row)
                    if num % 100000 == 0:
                        new_collection.insert_many(res)
                        res = []
                    self.loaded.emit(step, f'{lenght} документов')
                    if step < lenght-1:
                        step += 1
                if len(res) != 0:
                    new_collection.insert_many(res)
                step += 1
                self.loaded.emit(step, f'{lenght} документов')
                self.stop()
        self.finished.emit()

    def updateProgress(self, count, file):
        if not self.progress.wasCanceled():
            self.progress.setLabelText('Ожидается примерно %s' % os.path.basename(file))
            self.progress.setValue(count)

    def showProgress(self, text, length, handler):
        self.progress = QProgressDialog(text, "Отмена", 0, length)
        self.progress.setWindowModality(Qt.WindowModal)
        self.progress.canceled.connect(
            handler, type=Qt.DirectConnection)
        self.progress.forceShow()

    def stop(self):
        lenght = new_collection.find().count()
        w.set_data(lenght)
        self._stop = True


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
        self.ui.comboBox_2.currentIndexChanged.connect(self.change_size_butt)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.PathFile.setReadOnly(True)
        self.ui.OpenBox.currentIndexChanged.connect(self.openButt)
        self.ui.AnalizButt.clicked.connect(self.analizButt)
        self.ui.change_cbButt.clicked.connect(self.search_with_param)
        self.ui.saveButt.clicked.connect(self.save_Data)
        self.ui.DeleteButt.clicked.connect(self.delete_data)
        self.ui.UpdateButt.clicked.connect(self.update_data)
        self.callback_obj = SyncObj()
        self.callback_obj.progressBarUpdated.connect(self.ui.progressBar.setValue)
        self.callback_obj.tableUpdatedRow.connect(self.UpdateTableRow)
        self.callback_obj.tableUpdatedHeader.connect(self.UpdateTableHeader)
        self.setStyleSheet('QMainWindow { background-color: rgba(15, 19, 20, 0.82); color: white;}' 
                            'QScrollArea {border : 1px black; }'
                            'QTableWidget {background-color: rgba(15, 19, 20, 0.82); color: white; '
                            'border: 2px solid rgba(11, 33, 38, 0.96);  gridline-color: rgba(16, 74, 29, 0.96);'
                            'selection-background-color: rgba(13, 99, 5, 0.96); } '
                            'QHeaderView {background-color: rgba(15, 19, 20, 0.82); color: white; }'
                            'QHeaderView:section {background-color: rgba(15, 19, 20, 0.2); color: white; }'
                            'QPushButton { background-color: rgba(16, 74, 29, 0.96); color: white; }'
                            'QProgressBar:chunk {background-color: rgba(34, 242, 15, 0.96); }'
                            'QProgressBar { text-align: center; border: 2px solid rgba(11, 33, 38, 0.96); border-radius: 5px;'
                            'background-color: rgba(27, 51, 25, 0.96); color: white; }'
                            'QComboBox {background-color: rgba(16, 74, 29, 0.96); color: white; }'
                            'QScrollBar {border: 1px black; background-color: rgba(15, 19, 20, 0.82);}'
                            'QScrollBar:handle {background-color: rgba(19, 143, 31, 0.5); min-height: 30px; }'
                            'QScrollBar:up-arrow{width: 3px; height: 3px; background-color: black;}'
                            'QScrollBar:down-arrow{border: 1px black; width: 3px; height: 3px; background-color: black;}'
                            'QScrollBar:add-page {background-color: none;}'
                            'QScrollBar:sub-page {background-color: none;}')

    def locker(self):
        self.ui.AnalizButt.setDisabled(True)
        self.ui.saveButt.setDisabled(True)
        self.ui.change_cbButt.setDisabled(True)
        self.ui.DeleteButt.setDisabled(True)
        self.ui.UpdateButt.setDisabled(True)
        self.ui.OpenBox.setDisabled(True)

    def unlocker(self):
        self.ui.AnalizButt.setDisabled(False)
        self.ui.saveButt.setDisabled(False)
        self.ui.change_cbButt.setDisabled(False)
        self.ui.DeleteButt.setDisabled(False)
        self.ui.UpdateButt.setDisabled(False)
        self.ui.OpenBox.setDisabled(False)

    def locker1(self):
        self.ui.AnalizButt.setDisabled(True)

    def unlocker2(self):
        self.ui.AnalizButt.setDisabled(False)

    #Delete
    def delete_data(self):
        if self.chek:
            row = self.ui.tableWidget.currentRow()
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
            new_collection.delete_one(row1)
            QMessageBox.about(self, 'Успешно', 'Для просмотра изменений обновите выборку') 
        else:
            QMessageBox.about(self, 'Ошибка', 'Проанализируйте файл.')
        

    #Update
    def update_data(self):
        if self.chek:
            row = self.ui.tableWidget.currentRow()
            column = self.ui.tableWidget.currentColumn()
            value, ok = QInputDialog.getText(self, "Ввод нового значения", "Введите новое значение", QLineEdit.Normal,'')
            if value and ok:
                data = []
                row1 = {}
                for i in range(7):
                    item = self.ui.tableWidget.item(row, i).text()
                    data.append(item)
                header= ['number', 'name', 'fname', 'phone', 'uid', 'nik', 'wo']
                for i in range(7):
                    row2 = {}
                    row2 = {header[i] : data[i]}
                    row1.update(row2) 
                new_collection.update_one(row1, {"$set":{f'{header[column]}': f'{value}'}})
                QMessageBox.about(self, 'Успешно!', 'Для просмотра изменений обновите выборку')     
            else:
                QMessageBox.about(self, 'Ошибка', 'Введите данные.')
        else:
            QMessageBox.about(self, 'Ошибка', 'Проанализируйте файл.')

    #Save
    def save_Data(self):
        if self.chek:
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
        else:
            QMessageBox.about(self, 'Ошибка', 'Проанализируйте файл.')

    #Open
    def openButt(self):
        id = self.ui.OpenBox.currentIndex()
        if id == 1:
            fileD = QFileDialog()
            open_file = fileD.getExistingDirectory(self)
            self.ui.PathFile.setText('')
            self.ui.PathFile.setText(open_file)
            self.unlocker2()
        elif id ==2:
            str0, ok = QInputDialog.getText(self, "Ввод параметра", "Введите данные в виде: name|fname|phone|uid|nik|wo", QLineEdit.Normal,'')
            if str0 and ok:
                data = str0.split('|')
                if len(data) == 6:
                    res = []
                    row = {}
                    number = self.check_last_doc()
                    data.reverse()
                    data.append(f'{number + 1}')
                    data.reverse()
                    header= ['number', 'name', 'fname', 'phone', 'uid', 'nik', 'wo']
                    for i in range(7): 
                        row1 = {}
                        row1 = {header[i] : data[i]}
                        row.update(row1)
                    res.append(row)
                    new_collection.insert_many(res)
                    if number + 1 <= 100:
                        self.callback_obj.tableUpdatedRow.emit(number, 0, data)
                    else:
                        lenght = new_collection.find().count()
                        self.set_data(lenght)
                    self.chek = True
                else:
                    QMessageBox.about(self, 'Ошибка', 'Неверный формат данных')
                    self.unlocker()
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
        b = os.path.getsize(get_path)
        self.worker = Worker(csv_files, b)
        self.worker.run()
        self.locker1()

    def import_data(self, miim, maam):
        step = 0
        head = self.serch('number','№')
        self.UpdateTableHeader(head)
        self.ui.tableWidget.setRowCount(0)
        lim = maam - miim
        data = new_collection.find({}, { '_id' : 0}).skip(miim).limit(lim+1)
        i = miim
        for doc in data:
            one_doc = []
            for value in doc.values():
                one_doc.append(value)
            step += 1
            self.callback_obj.progressBarUpdated.emit(step)
            self.callback_obj.tableUpdatedRow.emit(i, miim, one_doc)
            i +=1
        self.callback_obj.progressBarUpdated.emit(step + 1)
        self.callback_obj.progressBarUpdated.emit(0)

    def serch(self, param, value):
        js = new_collection.find({param : value}, { '_id' : 0})
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
                    one_doc = self.serch('nik', value)
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
        miim, maaa = 1, 100
        if self.chek:
            try:
                miim_maam0 = self.ui.comboBox_2.currentText()
                miim_maam = miim_maam0.split(' - ')
                miim, maam = miim_maam[0], miim_maam[1]
            except IndexError:
                miim, maaa = 1, 100
                pass
        return int(miim), int(maam)

    def change_size_butt(self):
        miim, maam = self.change_size()
        self.import_data(miim, maam)

    def set_data(self, lenght):
        self.locker()
        miim, maam = 1, 100
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
        if ost != count_id * 100:
            self.ui.comboBox_2.addItem(f"{count_id * 100} - {ost}")
        self.unlocker()
        self.chek = True

    def check_last_doc(self):
        number = 0
        if self.chek:
            last_doc = new_collection.find().sort('_id', -1).limit(1)
            for doc in last_doc:
                one_doc = []
                for value in doc.values():
                    one_doc.append(value)
                one_doc.pop(0)
                number = one_doc[0]
        return int(number)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Win()
    w.show()
    sys.exit(app.exec_())