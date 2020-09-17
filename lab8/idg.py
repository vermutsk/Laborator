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
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1121, 770)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 1101, 531))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1099, 529))
        self.tableView = QTableView(self.scrollAreaWidgetContents)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(5, 1, 1091, 521))
        self.tableView.setAutoFillBackground(True)
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 610, 301, 28))
        self.progressBar_2 = QProgressBar(Dialog)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(400, 590, 651, 23))
        self.progressBar_2.setValue(24)
        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(400, 660, 651, 23))
        self.progressBar.setValue(40)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 690, 161, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setMinimumContentsLength(3)
        self.comboBox.setDuplicatesEnabled(False)
        self.pushButton_6 = QPushButton(Dialog)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 570, 301, 28))
        self.pushButton_7 = QPushButton(Dialog)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(20, 730, 301, 28))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(190, 650, 131, 31))
        self.pushButton_8 = QPushButton(Dialog)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 650, 161, 28))
        self.dateTimeEdit = QDateTimeEdit(Dialog)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(190, 690, 131, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(accessibility)
        self.tableView.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u043e\u0440\u043a\u0430 \u043f\u043e \u043b\u043e\u0433\u0438\u043d\u0443", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u043e\u0440\u043a\u0430 \u043f\u043e \u0434\u0430\u0442\u0435", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.comboBox.setPlaceholderText("")
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"\u0410\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c ", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"0-999", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c  \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b", None))
    # retranslateUi

