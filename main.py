import multiprocessing as mp
import os
import sys
import time

from PySide2 import QtCore
from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox, QTableWidgetItem)

import db
import front

g_max_value = 1
g_current_value = 0


class Transfer_to_main():
    def teleport(self, current_value, max_value):
        global g_max_value
        global g_current_value
        g_max_value = max_value
        g_current_value = current_value


class WorkerThread_bar(QThread):
    updateProgress = QtCore.Signal(int)

    def __init__(self, parent=None):
        QThread.__init__(self)

    def run(self):
        while g_current_value <= g_max_value:
            self.updateProgress.emit(db.get_percent())
        self.updateProgress.emit(100)

        return


class MyQtApp(front.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MyQtApp, self).__init__(parent)
        self.setupUi(self)

        self.progress_barchik.setValue(0)
        self.helper = db.Transfer_to_db()

        self.button_import.clicked.connect(self.open_file_browser)

    def open_file_browser(self):
        global g_max_value
        global g_current_value

        print("open_file_browser")

        g_path_to_csv = QFileDialog.getOpenFileName()[0]

        if not g_path_to_csv:
            print("файл не был выбран")
        else:
            self.helper.teleport(g_path_to_csv)

            self.workerThread = db.WorkerThread()
            self.workerThread.start()

            self.workerBar = WorkerThread_bar()
            self.workerBar.updateProgress.connect(self.setProgress)
            self.workerBar.start()

    def setProgress(self, progress):
        self.progress_barchik.setValue(progress)


def main():
    app = QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()


if __name__ == '__main__':
    main()
