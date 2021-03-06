# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import (QScrollArea, QWidget, QTableWidget, QPushButton,
    QProgressBar, QComboBox, QLineEdit, QDateTimeEdit)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 770)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea = QScrollArea(MainWindow)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 1101, 531))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1099, 529))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 1099, 529))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.setColumnCount(24) 
        self.column_label = ['begin', 'end', 'time interval', 'login', 'mac ab', 'ULSK1', 'BRAS ip', 'start count', 'alive count',
                            'stop count', 'incoming', 'outcoming', 'error_count', 'code 0', 'code 1011', 'code 1100', 'code -3',
                            'code -52', 'code -42', 'code -21', 'code -40', ' code -44', 'code -46', ' code -38']
        self.tableWidget.setHorizontalHeaderLabels(self.column_label)
        
        self.PathFile = QLineEdit(self.centralwidget)
        self.PathFile.setGeometry(QRect(200, 10, 831, 90))
        self.PathFile.setObjectName("PathFile")

        self.progressBar_2 = QProgressBar(MainWindow)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_2.setGeometry(QRect(400, 590, 651, 23))
        self.progressBar_2.setProperty("value", 0)

        self.progressBar = QProgressBar(MainWindow)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setGeometry(QRect(400, 650, 651, 23))
        self.progressBar.setProperty("value", 0)

        self.comboBox = QComboBox(MainWindow)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(20, 690, 161, 28))
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(False)

        self.dateTimeEdit = QDateTimeEdit(MainWindow)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(190, 690, 151, 28))
        self.dateTimeEdit.setCurrentSection(QDateTimeEdit.DaySection)
        

        self.saveButt = QPushButton(self.centralwidget)
        self.saveButt.setGeometry(QRect(20, 610, 321, 28))
        self.saveButt.setObjectName("saveButt")

        self.AnalizButt = QPushButton(self.centralwidget)
        self.AnalizButt.setGeometry(QRect(20, 570, 321, 28))
        self.AnalizButt.setObjectName("AnalizButt")
        
        self.OpenButt = QPushButton(self.centralwidget)
        self.OpenButt.setGeometry(QRect(400, 710, 615, 40))
        self.OpenButt.setObjectName("OpenButt")

        self.change_cbButt = QPushButton(self.centralwidget)
        self.change_cbButt.setObjectName("change_cbButt")
        self.change_cbButt.setGeometry(QRect(20, 730, 321, 28))

        self.change_sizeButt = QPushButton(self.centralwidget)
        self.change_sizeButt.setObjectName(u"change_sizeButt")
        self.change_sizeButt.setGeometry(QRect(20, 650, 161, 28))

        self.change_sizeLine = QLineEdit(self.centralwidget)
        self.change_sizeLine.setObjectName("change_sizeLine")
        self.change_sizeLine.setGeometry(QRect(190, 650, 151, 28))

        self.OpenButt.raise_()
        self.AnalizButt.raise_()
        self.change_cbButt.raise_()
        self.progressBar.raise_()
        self.PathFile.raise_()
        self.tableWidget.raise_()
        self.saveButt.raise_()
        self.comboBox.raise_()
        self.dateTimeEdit.raise_()
        self.change_sizeButt.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
#if QT_CONFIG(accessibility)
        self.tableWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", "Парамметры выборки", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", "Выборка по логину", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", "Выборка по дате", None))
        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", "\u041f\u043e\u043b\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.comboBox.setPlaceholderText("")
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", "dd.MM.yyyy H:mm:ss"))
        self.saveButt.setText(QCoreApplication.translate("MainWindow", "Сохранить данные", None))
        self.OpenButt.setText(QCoreApplication.translate("MainWindow", "Выбрать папку", None))
        self.change_cbButt.setText(QCoreApplication.translate("MainWindow", "Изменить парамметры", None))
        self.AnalizButt.setText(QCoreApplication.translate("MainWindow", "Анализировать", None))
        self.change_sizeLine.setPlaceholderText(QCoreApplication.translate("MainWindow", "1-1000", None))
        self.change_sizeButt.setText(QCoreApplication.translate("MainWindow", u"Изменить выборку", None))
    # retranslateUi

