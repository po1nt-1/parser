import multiprocessing as mp
import os
import sys
import time

from PySide2 import QtCore
from PySide2.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox, QTableWidgetItem)

import db
import front


class MyQtApp(front.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MyQtApp, self).__init__(parent)
        self.setupUi(self)

        self.button_import.clicked.connect(self.open_file_browser)

    def open_file_browser(self):
        print("open_file_browser")

        g_path_to_csv = QFileDialog.getOpenFileName()[0]

        if not g_path_to_csv:
            print("файл не был выбран")
        else:
            db.Transfer(g_path_to_csv)
            self.workerThread = db.WorkerThread()
            self.workerThread.start()


def main():
    app = QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()


if __name__ == '__main__':
    main()
