import inspect
import json
import multiprocessing as mp
import os
import sys
import time

import pymongo
from bson import errors
from pymongo import MongoClient
from PySide2 import QtCore
from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox, QTableWidgetItem)

import front

g_path_to_csv = ""

g_max_value = 1
g_current_value = 0

g_active_import = False
g_active_export = False


class local_error(Exception):
    pass


class Worker_bar(QThread):
    updateProgress = Signal(int)

    def __init__(self, parent=None):
        QThread.__init__(self)

    def run(self):
        global g_active_import
        global g_current_value
        global g_max_value

        while g_current_value <= g_max_value:
            if g_active_import:
                self.updateProgress.emit(get_percent())


class Worker_importer(QThread):
    def __init__(self, parent=None):
        super(Worker_importer, self).__init__(parent)

    def run(self):
        global g_path_to_csv

        collection = init_collection()
        import_data(collection, g_path_to_csv)


class MyQtApp(front.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MyQtApp, self).__init__(parent)
        self.setupUi(self)

        self.worker_importer = Worker_importer()
        self.worker_bar = Worker_bar()

        self.progress_barchik.setValue(0)

        self.button_import.clicked.connect(self.open_file_browser)
        self.button_export.clicked.connect(self.export)
        self.button_stop.clicked.connect(self.stop)
        self.button_back.clicked.connect(self.back)
        self.button_forward.clicked.connect(self.forward)

    def open_file_browser(self):
        global g_max_value
        global g_current_value
        global g_path_to_csv

        global g_active_import

        g_active_import = False

        print("open_file_browser")

        g_path_to_csv = QFileDialog.getOpenFileName()[0]

        if not g_path_to_csv:
            print("файл не был выбран")
        else:

            self.worker_bar.updateProgress.connect(self.setProgress)

            self.worker_importer.start()
            self.worker_bar.start()

    def setProgress(self, progress):
        self.progress_barchik.setValue(progress)

    def export(self):
        print("ну экспорт")

    def back(self):
        print("ну назад")

    def forward(self):
        print("ну вперёд")

    def stop(self):
        global g_active_import
        global g_active_export

        g_active_import = False
        g_active_export = False


# class Worker_exporter(QThread):
#     def __init__(self, parent=None):
#         super(Worker_exporter, self).__init__(parent)

#     def run(self):
#         collection = init_collection()
#         export_data()


def get_percent():
    global g_current_value
    global g_max_value

    if g_max_value == 0:
        return 100

    per = 100 * float(g_current_value)/float(g_max_value)
    return int(per)


def get_script_dir(follow_symlinks=True):
    '''получить директорию со исполняемым скриптом'''
    # https://clck.ru/P8NUA
    if getattr(sys, 'frozen', False):  # type: ignore
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def init_collection():
    client = MongoClient()
    db = client["db"]
    collection = db["collection"]

    return collection


def insert(collection, data):
    try:
        if not isinstance(data, list):
            collection.insert_one(data)
        else:
            collection.insert_many(data)
    except errors.InvalidDocument as e:
        raise local_error(str(e))


def find(collection, _id="", fname="", phone="", nik="", skip=0, limit=0):
    try:
        request = {}
        if _id != "":
            request.update({"_id": str(_id)})
        if fname != "":
            request.update({"fname": str(fname)})
        if phone != "":
            request.update({"phone": str(phone)})
        if nik != "":
            request.update({"nik": str(nik)})

        c = collection.find(request, skip=skip, limit=limit)

        data = [i for i in c]
    except pymongo.errors.OperationFailure as e:
        raise local_error(str(e))
    return data


def replace(collection, _id, data):
    data_pull = find(collection, _id=_id, limit=1)[0]
    data_pull.update(data)

    collection.replace_one({'_id': str(_id)}, data_pull)


def delete(collection, data):
    collection.delete_one(data)


def gen_new_csv_name():
    path = os.path.join(get_script_dir(), "get_csv_here")
    if not os.path.exists(path):
        os.mkdir(path)
    files = os.listdir(path)
    i = 1
    while f"result{i}.csv" in files:
        i += 1
    return f"result{i}.csv"


def import_data(collection, path):
    global g_max_value
    global g_current_value

    global g_active_import

    g_active_import = True

    try:
        if not os.path.exists(path):
            raise local_error("path doesn't exists")

        collection.drop()

        headers = ['_id', 'name', 'fname', 'phone', 'uid', 'nik', 'wo']

        print("считываю длину файла..", end="")
        with open(path, 'r', encoding="Windows-1251") as f:
            g_max_value = sum(1 for _ in f) - 1
            print(".")

        with open(path, 'r', encoding="Windows-1251") as f:
            f.readline()
            g_current_value = 0
            block = 10000
            data = []

            from time import time
            start = time()

            for line in f:
                g_current_value += 1
                if line.isspace():
                    continue

                line = line[1:-2].split("|")[:7]
                iter_data = {}
                for i, item in enumerate(line):
                    iter_data.update({headers[i]: str(item)})

                data.append(iter_data)

                if g_current_value % block == 0:
                    data.sort(key=lambda field: field['_id'])
                    insert(collection, data)

                    data = []

                elif g_current_value >= g_max_value:
                    data.sort(key=lambda field: field['_id'])
                    insert(collection, data)

                    iter_data = {}
                    data = []

                if not g_active_import:
                    break

        print("import закончен")

        eee = str((time() - start) / 60).split(".")
        print(eee[0] + "." + eee[1][:3] + " min")
    finally:
        g_active_import = False


def export_data(collection, path, data_in):
    data_out = []
    with open(path, 'w', encoding="utf-8") as f:
        data_out.append("_id,name,fname,phone,uid,nik,wo\n")
        for line in data_in:
            data_out.append(f'{line["_id"]},{line["name"]},' +
                            f'{line["fname"]},{line["phone"]},' +
                            f'{line["uid"]},{line["nik"]},{line["wo"]}\n')
        f.writelines(data_out)
        data_in.clear()
        data_out.clear()


def common_check(data):
    if isinstance(data, str):
        if "," in data or "|" in data or "\n" in data:
            raise local_error(f"'{data}' contains an unsupported symbol")
    else:
        raise local_error(f"'{data}' is not a string")


def main():
    app = QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()


if __name__ == '__main__':
    main()
