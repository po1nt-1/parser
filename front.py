# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 675)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 675))
        MainWindow.setMaximumSize(QSize(1200, 675))
        font = QFont()
        font.setFamily(u"Open Sans Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"color: rgb(27, 29, 35);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_fname = QLineEdit(self.centralwidget)
        self.lineEdit_fname.setObjectName(u"lineEdit_fname")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(240)
        sizePolicy1.setVerticalStretch(40)
        sizePolicy1.setHeightForWidth(self.lineEdit_fname.sizePolicy().hasHeightForWidth())
        self.lineEdit_fname.setSizePolicy(sizePolicy1)
        self.lineEdit_fname.setMinimumSize(QSize(240, 40))
        self.lineEdit_fname.setMaximumSize(QSize(240, 40))
        font1 = QFont()
        font1.setFamily(u"Open Sans Light")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.lineEdit_fname.setFont(font1)
        self.lineEdit_fname.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")
        self.lineEdit_fname.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_fname.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit_fname)

        self.lineEdit_nik = QLineEdit(self.centralwidget)
        self.lineEdit_nik.setObjectName(u"lineEdit_nik")
        sizePolicy1.setHeightForWidth(self.lineEdit_nik.sizePolicy().hasHeightForWidth())
        self.lineEdit_nik.setSizePolicy(sizePolicy1)
        self.lineEdit_nik.setMinimumSize(QSize(240, 40))
        self.lineEdit_nik.setMaximumSize(QSize(240, 40))
        self.lineEdit_nik.setFont(font1)
        self.lineEdit_nik.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")
        self.lineEdit_nik.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit_nik)

        self.lineEdit_phone = QLineEdit(self.centralwidget)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")
        sizePolicy1.setHeightForWidth(self.lineEdit_phone.sizePolicy().hasHeightForWidth())
        self.lineEdit_phone.setSizePolicy(sizePolicy1)
        self.lineEdit_phone.setMinimumSize(QSize(240, 40))
        self.lineEdit_phone.setMaximumSize(QSize(240, 40))
        self.lineEdit_phone.setFont(font1)
        self.lineEdit_phone.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")
        self.lineEdit_phone.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit_phone)

        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(240)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy2)
        self.pushButton_1.setMinimumSize(QSize(240, 40))
        self.pushButton_1.setMaximumSize(QSize(240, 40))
        self.pushButton_1.setFont(font1)
        self.pushButton_1.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_1.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(240, 40))
        self.pushButton_2.setMaximumSize(QSize(240, 40))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.rowCount() < 100):
            self.tableWidget.setRowCount(100)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(900, 550))
        self.tableWidget.setMaximumSize(QSize(900, 550))
        font2 = QFont()
        font2.setFamily(u"Open Sans Light")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(True)
        font2.setUnderline(False)
        font2.setWeight(3)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.tableWidget.setFont(font2)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QTableWidget:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QTableWidget:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(160, 40))
        self.pushButton_3.setMaximumSize(QSize(160, 40))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.plainTextEdit_pages_current = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_pages_current.setObjectName(u"plainTextEdit_pages_current")
        self.plainTextEdit_pages_current.setMinimumSize(QSize(70, 40))
        self.plainTextEdit_pages_current.setMaximumSize(QSize(70, 40))
        self.plainTextEdit_pages_current.setFont(font1)
        self.plainTextEdit_pages_current.setStyleSheet(u"QPlainTextEdit {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")
        self.plainTextEdit_pages_current.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhMultiLine)
        self.plainTextEdit_pages_current.setReadOnly(True)

        self.horizontalLayout.addWidget(self.plainTextEdit_pages_current)

        self.label_pages_current = QLabel(self.centralwidget)
        self.label_pages_current.setObjectName(u"label_pages_current")
        self.label_pages_current.setMinimumSize(QSize(70, 40))
        self.label_pages_current.setMaximumSize(QSize(70, 40))
        self.label_pages_current.setFont(font1)
        self.label_pages_current.setStyleSheet(u"QLabel {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QLabel:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLabel:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")

        self.horizontalLayout.addWidget(self.label_pages_current)

        self.plainTextEdit_pages_max = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_pages_max.setObjectName(u"plainTextEdit_pages_max")
        self.plainTextEdit_pages_max.setMinimumSize(QSize(70, 40))
        self.plainTextEdit_pages_max.setMaximumSize(QSize(70, 40))
        self.plainTextEdit_pages_max.setFont(font1)
        self.plainTextEdit_pages_max.setStyleSheet(u"QPlainTextEdit {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")
        self.plainTextEdit_pages_max.setInputMethodHints(Qt.ImhMultiLine)
        self.plainTextEdit_pages_max.setReadOnly(True)

        self.horizontalLayout.addWidget(self.plainTextEdit_pages_max)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(160, 40))
        self.pushButton_4.setMaximumSize(QSize(160, 40))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"parser", None))
        self.lineEdit_fname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"fname", None))
        self.lineEdit_nik.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nik", None))
        self.lineEdit_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"phone", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 \u0411\u0414", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 CSV", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.plainTextEdit_pages_current.setPlainText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_pages_current.setText(QCoreApplication.translate("MainWindow", u"\u0438\u0437", None))
        self.plainTextEdit_pages_max.setPlainText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0451\u0434", None))
    # retranslateUi

