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
        MainWindow.resize(1121, 700)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea = QScrollArea(MainWindow)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 1100, 531))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1100, 529))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 1100, 529))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.setColumnCount(7) 
        self.column_label = ['№', 'name', 'fname', 'phone', 'uid', 'nik', 'wo']
        self.tableWidget.setHorizontalHeaderLabels(self.column_label)
        
        self.PathFile = QLineEdit(self.centralwidget)
        self.PathFile.setGeometry(QRect(200, 10, 831, 90))
        self.PathFile.setObjectName("PathFile")

        self.progressBar = QProgressBar(MainWindow)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setGeometry(QRect(400, 650, 678, 28))
        self.progressBar.setProperty("value", 0)

        self.comboBox = QComboBox(MainWindow)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(20, 610, 321, 28))
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(False)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QRect(20, 570, 321, 28))
        self.comboBox_2.setObjectName("comboBox2")
        self.comboBox_2.addItem("")

        self.saveButt = QPushButton(self.centralwidget)
        self.saveButt.setGeometry(QRect(560, 610, 160, 28))
        self.saveButt.setObjectName("saveButt")

        self.AnalizButt = QPushButton(self.centralwidget)
        self.AnalizButt.setGeometry(QRect(400, 610, 160, 28))
        self.AnalizButt.setObjectName("AnalizButt")

        self.UpdateButt = QPushButton(self.centralwidget)
        self.UpdateButt.setGeometry(QRect(720, 610, 160, 28))
        self.UpdateButt.setObjectName("updateButt")

        self.DeleteButt = QPushButton(self.centralwidget)
        self.DeleteButt.setGeometry(QRect(880, 610, 160, 28))
        self.DeleteButt.setObjectName("DeleteButt")

        self.OpenBox = QComboBox(MainWindow)
        self.OpenBox.addItem("")
        self.OpenBox.addItem("")
        self.OpenBox.addItem("")
        self.OpenBox.setObjectName("OpenBox")
        self.OpenBox.setGeometry(QRect(400, 570, 160, 30))
        self.OpenBox.setEditable(False)
        self.OpenBox.setDuplicatesEnabled(False)
    
        self.change_cbButt = QPushButton(self.centralwidget)
        self.change_cbButt.setObjectName("change_cbButt")
        self.change_cbButt.setGeometry(QRect(20, 650, 321, 28))

        self.OpenBox.raise_()
        self.UpdateButt.raise_()
        self.AnalizButt.raise_()
        self.DeleteButt.raise_()
        self.change_cbButt.raise_()
        self.progressBar.raise_()
        self.PathFile.raise_()
        self.tableWidget.raise_()
        self.saveButt.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
#if QT_CONFIG(accessibility)
        self.tableWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", "Поиск по ...", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", "Поиск по никнейму", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", "Поиск по номеру телефона", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", "Поиск по фамилии", None))
        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", "\u041f\u043e\u043b\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.comboBox.setPlaceholderText("")
        self.saveButt.setText(QCoreApplication.translate("MainWindow", "Сохранить данные", None))
        self.OpenBox.setItemText(0, QCoreApplication.translate("MainWindow", "Загрузить данные", None))
        self.OpenBox.setItemText(1, QCoreApplication.translate("MainWindow", "Выбрать папку", None))
        self.OpenBox.setItemText(2, QCoreApplication.translate("MainWindow", "Ввести данные", None))
        self.change_cbButt.setText(QCoreApplication.translate("MainWindow", "Изменить парамметры", None))
        self.DeleteButt.setText(QCoreApplication.translate("MainWindow", "Удалить данные", None))
        self.UpdateButt.setText(QCoreApplication.translate("MainWindow", "Обновить данные", None))
        self.AnalizButt.setText(QCoreApplication.translate("MainWindow", "Анализировать", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", "1 - 100", None))
        
    # retranslateUi

