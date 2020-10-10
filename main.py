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


class DownloadCodesTask(QtCore.QThread):
    signal_progress_value = QtCore.Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        global g_path_to_csv

        print("run")
        print("# Ваш код")

        print("importing")
        collection = db.init_collection()
        db.import_data(collection, os.path.join(
            db.get_script_dir(), g_path_to_csv))

        print("imported")

        self.signal_progress_value.emit("какая-то строка передалась из run()")


class MyQtApp(front.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        # self.button_import.clicked.connect(
        #     self.import_to_db)
        self.button_forward.clicked.connect(self.forward)
        self.button_back.clicked.connect(self.back)

        self.button_import.clicked.connect(self.open_file_browser)

        self.progressThread = DownloadCodesTask()
        self.progressThread.signal_progress_value.connect(
            self.download_codes_handler)

    def open_file_browser(self):
        global g_path_to_csv

        print("open_file_browser")

        g_path_to_csv = QFileDialog.getOpenFileName()[0]

        if not g_path_to_csv:
            print("файл не выбран")
        else:
            print("# Запуск потока")
            self.progressThread.start()

    QtCore.Slot(str)

    def download_codes_handler(self, string):
        print("download_codes_handler")
        print("# Обработка сигнала")

        print(string)

    # def import_to_db(self):
    #     path = QFileDialog.getOpenFileName()[0]
    #     if not path:
    #         print("файл не выбран")
    #     else:
    #         print("importing")
    #         collection = db.init_collection()
    #         db.import_data(collection, os.path.join(
    #             db.get_script_dir(), path))

    #         print("imported")

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
