import multiprocessing as mp
import os
import sys

from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox, QTableWidgetItem)

import db
import front
import time


g_path_to_csv = ""


class MyQtApp(front.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.button_import.clicked.connect(
            self.import_to_db)
        self.button_forward.clicked.connect(self.forward)
        self.button_back.clicked.connect(self.back)

    def open_file_browser(self):
        global g_path_to_csv

        print("open_file_browser")

        g_path_to_csv = QFileDialog.getOpenFileName()[0]

    def forward(self):
        print("forward")

    def back(self):
        print("back")


def main():
    app = QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()


if __name__ == '__main__':
    main()
