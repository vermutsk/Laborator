import sys
import time
from PySide2 import QtGui, QtWidgets, QtCore, QtGui
from PySide2.QtCore import *
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget

class TadleWidgetWindow(object):
    def setapUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.resize(500, 500)
        vbox = QVBoxLayout(self.centralWidget)
        self.TabletWidget = QTableWidget()
        vbox.addWidget(self.TabletWidget)
        self.TabletWidget.setColumnCount(17)
        list1 = ['1', '2', '3', '4']
        l = [i for i in range(len(list1))]           #Длина списка
        self.TabletWidget.setRowCount(l) 
        self.column_label = ['begin', 'end', 'time interval', 'login', 'mac ab','ULSK1',\
                            'BRAS ip', ', start count', 'alive count', 'stop count', \
                            'incoming', 'outcoming', 'error_count','code 0', 'code 1011',\
                             'code 1100', 'code -3', 'code -52', 'code -42', 'code -21', \
                             ', code -40', 'code -44', 'code -46', 'code -38']
        self.row_label = l
        self.TabletWidget.HorizontalHeaderLadels(self.column_label)
        self.TabletWidget.VerticalHeaderLadels(self.row_label)
        self.TabletWidget.setSortingEnabled(True)

class MainWindow(QMainWindow, TadleWidgetWindow):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)

def main_application():
    '''
    функция для инициализации и отображения нашего основного окна приложения
    '''

    app = QApplication(sys.argv)  
    app.setStyle('cleanlooks')

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main_application()



