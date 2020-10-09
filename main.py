import os
import sys

from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox, QTableWidgetItem)

import db
import front


class MyQtApp(front.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.button_import.clicked.connect(
            self.import_to_db)
        self.button_forward.clicked.connect(self.forward)
        self.button_back.clicked.connect(self.back)

    def import_to_db(self):
        print("import")
        path = QFileDialog.getOpenFileName()[0]
        print(path)
        if not path:
            print("файл не выбран")
        else:
            collection = db.init_collection()
            db.import_data(collection, os.path.join(
                db.get_script_dir(), path))
            print("imported")

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
