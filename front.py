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
"color: #FFF;")
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
        sizePolicy.setHeightForWidth(self.lineEdit_fname.sizePolicy().hasHeightForWidth())
        self.lineEdit_fname.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.lineEdit_nik.sizePolicy().hasHeightForWidth())
        self.lineEdit_nik.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.lineEdit_phone.sizePolicy().hasHeightForWidth())
        self.lineEdit_phone.setSizePolicy(sizePolicy)
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

        self.button_import = QPushButton(self.centralwidget)
        self.button_import.setObjectName(u"button_import")
        sizePolicy.setHeightForWidth(self.button_import.sizePolicy().hasHeightForWidth())
        self.button_import.setSizePolicy(sizePolicy)
        self.button_import.setMinimumSize(QSize(240, 40))
        self.button_import.setMaximumSize(QSize(240, 40))
        self.button_import.setFont(font1)
        self.button_import.setFocusPolicy(Qt.StrongFocus)
        self.button_import.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.button_import)

        self.button_show = QPushButton(self.centralwidget)
        self.button_show.setObjectName(u"button_show")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(240)
        sizePolicy1.setVerticalStretch(40)
        sizePolicy1.setHeightForWidth(self.button_show.sizePolicy().hasHeightForWidth())
        self.button_show.setSizePolicy(sizePolicy1)
        self.button_show.setMinimumSize(QSize(240, 40))
        self.button_show.setMaximumSize(QSize(240, 40))
        font2 = QFont()
        font2.setFamily(u"Open Sans Light")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.button_show.setFont(font2)
        self.button_show.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.button_show)

        self.button_export = QPushButton(self.centralwidget)
        self.button_export.setObjectName(u"button_export")
        sizePolicy.setHeightForWidth(self.button_export.sizePolicy().hasHeightForWidth())
        self.button_export.setSizePolicy(sizePolicy)
        self.button_export.setMinimumSize(QSize(240, 40))
        self.button_export.setMaximumSize(QSize(240, 40))
        self.button_export.setFont(font1)
        self.button_export.setFocusPolicy(Qt.StrongFocus)
        self.button_export.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.button_export)


        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        if (self.tableWidget.rowCount() < 100):
            self.tableWidget.setRowCount(100)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(810, 450))
        self.tableWidget.setMaximumSize(QSize(810, 450))
        self.tableWidget.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setFamily(u"Open Sans Light")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(True)
        font3.setUnderline(False)
        font3.setWeight(50)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.tableWidget.setFont(font3)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"    padding: 4px;\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: rgb(48, 50, 62);\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}")
        self.tableWidget.setGridStyle(Qt.DashLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(112)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_9 = QSpacerItem(64, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.button_back = QPushButton(self.centralwidget)
        self.button_back.setObjectName(u"button_back")
        self.button_back.setMinimumSize(QSize(0, 40))
        self.button_back.setMaximumSize(QSize(160, 40))
        self.button_back.setFont(font1)
        self.button_back.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.button_back)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.lineEdit_pages_cur = QLineEdit(self.centralwidget)
        self.lineEdit_pages_cur.setObjectName(u"lineEdit_pages_cur")
        self.lineEdit_pages_cur.setMinimumSize(QSize(100, 40))
        self.lineEdit_pages_cur.setMaximumSize(QSize(100, 40))
        self.lineEdit_pages_cur.setFont(font2)
        self.lineEdit_pages_cur.setFocusPolicy(Qt.NoFocus)
        self.lineEdit_pages_cur.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")
        self.lineEdit_pages_cur.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_pages_cur.setMaxLength(9)
        self.lineEdit_pages_cur.setReadOnly(True)
        self.lineEdit_pages_cur.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit_pages_cur)

        self.label_static = QLabel(self.centralwidget)
        self.label_static.setObjectName(u"label_static")
        self.label_static.setMinimumSize(QSize(70, 40))
        self.label_static.setMaximumSize(QSize(70, 40))
        self.label_static.setFont(font1)
        self.label_static.setStyleSheet(u"QLabel {\n"
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

        self.horizontalLayout.addWidget(self.label_static)

        self.lineEdit_pages_max = QLineEdit(self.centralwidget)
        self.lineEdit_pages_max.setObjectName(u"lineEdit_pages_max")
        self.lineEdit_pages_max.setMinimumSize(QSize(100, 40))
        self.lineEdit_pages_max.setMaximumSize(QSize(100, 40))
        self.lineEdit_pages_max.setFont(font2)
        self.lineEdit_pages_max.setMouseTracking(True)
        self.lineEdit_pages_max.setFocusPolicy(Qt.NoFocus)
        self.lineEdit_pages_max.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")
        self.lineEdit_pages_max.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_pages_max.setMaxLength(9)
        self.lineEdit_pages_max.setReadOnly(True)
        self.lineEdit_pages_max.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_pages_max.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit_pages_max)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.button_forward = QPushButton(self.centralwidget)
        self.button_forward.setObjectName(u"button_forward")
        self.button_forward.setMinimumSize(QSize(160, 40))
        self.button_forward.setMaximumSize(QSize(160, 40))
        self.button_forward.setFont(font1)
        self.button_forward.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.button_forward)

        self.horizontalSpacer_10 = QSpacerItem(64, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.progress_barchik = QProgressBar(self.centralwidget)
        self.progress_barchik.setObjectName(u"progress_barchik")
        sizePolicy.setHeightForWidth(self.progress_barchik.sizePolicy().hasHeightForWidth())
        self.progress_barchik.setSizePolicy(sizePolicy)
        self.progress_barchik.setMinimumSize(QSize(810, 40))
        self.progress_barchik.setMaximumSize(QSize(810, 40))
        font4 = QFont()
        font4.setFamily(u"Open Sans ExtraBold")
        font4.setPointSize(25)
        font4.setBold(True)
        font4.setWeight(75)
        self.progress_barchik.setFont(font4)
        self.progress_barchik.setCursor(QCursor(Qt.BusyCursor))
        self.progress_barchik.setStyleSheet(u"QProgressBar {\n"
"    border: 0.5px solid rgb(48, 50, 62);\n"
"    text-align: right;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(85, 170, 255);\n"
"    width: 5px;\n"
"    margin: 0.5px;\n"
"}")
        self.progress_barchik.setValue(0)
        self.progress_barchik.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_2.addWidget(self.progress_barchik)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_5 = QSpacerItem(718, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.button_stop = QPushButton(self.centralwidget)
        self.button_stop.setObjectName(u"button_stop")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_stop.sizePolicy().hasHeightForWidth())
        self.button_stop.setSizePolicy(sizePolicy2)
        self.button_stop.setMinimumSize(QSize(160, 40))
        self.button_stop.setMaximumSize(QSize(160, 40))
        self.button_stop.setFont(font1)
        self.button_stop.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 20px;\n"
"	color: #FFF;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(200, 0, 0);\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_stop)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


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
        self.button_import.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 \u0411\u0414", None))
        self.button_show.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.button_export.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 CSV", None))
        self.button_back.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.lineEdit_pages_cur.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_static.setText(QCoreApplication.translate("MainWindow", u"\u0438\u0437", None))
        self.lineEdit_pages_max.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_forward.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0451\u0434", None))
        self.button_stop.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f", None))
    # retranslateUi

