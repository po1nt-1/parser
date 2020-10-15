import inspect
import json
import multiprocessing as mp
import os
import re
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

g_overload_param = ""

g_max_value = 2
g_current_value = 0

g_active_import = False
g_active_export = False

g_collection = ""

headers = ['_id', 'name', 'fname', 'phone', 'uid', 'nik', 'wo']

g_page_number = 1
g_pages_total = 1


class Local_error(Exception):
    pass


class Worker_bar(QThread):
    updateProgress = Signal(int)

    def __init__(self, parent=None):
        super(Worker_bar, self).__init__(parent)

    def run(self):
        global g_active_import
        global g_current_value
        global g_max_value

        while g_current_value <= g_max_value:
            if g_active_import:
                self.updateProgress.emit(get_percent())

        print("если это видно, значит проблема с QThread решилась")


class Worker_Boris(QThread):
    def __init__(self, parent=None):
        super(Worker_Boris, self).__init__(parent)

    def run(self):
        global g_overload_param
        global g_path_to_csv
        global g_collection

        try:
            if g_overload_param == "import":
                import_data(g_collection, g_path_to_csv)
            elif g_overload_param == "export":
                pass  # export
        except Local_error as e:
            pass


class MyQtApp(front.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MyQtApp, self).__init__(parent)
        self.setupUi(self)

        self.worker_importer = Worker_Boris()
        self.worker_bar = Worker_bar()
        init_collection()

        self.progress_barchik.setValue(0)
        self.notifier = QMessageBox()

        self.button_import.clicked.connect(self.open_file_browser)
        self.button_show.clicked.connect(self.show_table)
        self.button_export.clicked.connect(self.export)
        self.button_update.clicked.connect(self.update)
        self.button_insert.clicked.connect(self.insert)
        self.button_delete.clicked.connect(self.delete)
        self.button_forward.clicked.connect(self.forward)
        self.button_back.clicked.connect(self.back)
        self.button_stop.clicked.connect(self.stop)

        #           ###  ###############  #           ###
        #       ####     #                #       ####
        # ######         ###############  # ######
        #       ####     #                #       ####
        #           ###  ###############  #           ###

    def open_file_browser(self):
        try:
            global g_path_to_csv
            global g_overload_param

            global g_active_import

            global g_page_number
            global g_pages_total

            g_path_to_csv = QFileDialog.getOpenFileName()[0]

            if not g_path_to_csv:
                raise Local_error("Путь не выбран")
            else:
                g_page_number = 1
                g_pages_total = 1
                self.lineEdit_pages_cur.setText(str(g_page_number))
                self.lineEdit_pages_max.setText(str(g_pages_total))
                self.tableWidget.clear()

                g_active_import = False

                self.progress_barchik.setValue(0)
                self.worker_bar.updateProgress.connect(self.setProgress)

                g_overload_param = "import"
                self.worker_importer.start()
                self.worker_bar.start()
        except Local_error as e:
            self.notifier.about(self, " ", str(e))

    def setProgress(self, progress):
        try:
            global g_active_import
            if g_active_import:
                self.progress_barchik.setValue(progress)
        except Local_error as e:
            self.notifier.about(self, " ", str(e))

    def show_table(self):
        try:
            global g_collection
            global g_page_number
            global g_pages_total

            g_page_number = 1
            g_pages_total = 1

            self.tableWidget.clear()
            self.tableWidget.setHorizontalHeaderLabels(headers)

            self.name = str(self.lineEdit_name.text())
            self.fname = str(self.lineEdit_fname.text())
            self.phone = str(self.lineEdit_phone.text())
            self.uid = str(self.lineEdit_uid.text())
            self.nik = str(self.lineEdit_nik.text())
            self.wo = str(self.lineEdit_wo.text())

            input_check(self.name)
            input_check(self.fname)
            input_check(self.phone)
            input_check(self.uid)
            input_check(self.nik)
            input_check(self.wo)

            if self.name or self.fname or self.phone or \
                    self.uid or self.nik or self.wo:
                response = find(g_collection,
                                name=self.name,
                                fname=self.fname,
                                phone=self.phone,
                                uid=self.uid,
                                nik=self.nik,
                                wo=self.wo)
                collection_len = len(response)
            else:
                response = find(g_collection, skip=0, limit=100)
                collection_len = g_collection.estimated_document_count()

            if len(response) == 0:
                raise Local_error("Данные отсутствуют")

            if collection_len / 100 > 1:
                if collection_len % 100 == 0:
                    g_pages_total = collection_len // 100
                else:
                    g_pages_total = collection_len // 100 + 1
            else:
                g_pages_total = 1

            self.lineEdit_pages_cur.setText(str(g_page_number))
            self.lineEdit_pages_max.setText(str(g_pages_total))

            for row_number, row_value in enumerate(response):
                for item_number, item_value in enumerate(row_value):
                    self.tableWidget.setItem(
                        row_number, item_number, QTableWidgetItem(
                            str(list(row_value.values())[item_number]))
                    )
                    self.tableWidget.horizontalHeaderItem(
                        item_number).setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget.resizeColumnsToContents()
        except Local_error as e:
            self.notifier.about(self, " ", str(e))

    def update(self):
        pass

    def export(self):
        try:
            print("экспорт")
        except Local_error as e:
            self.notifier.about(self, " ", str(e))

    def insert(self):
        try:
            global g_collection
            print("вставить")

            self.name = str(self.lineEdit_name.text())
            self.fname = str(self.lineEdit_fname.text())
            self.phone = str(self.lineEdit_phone.text())
            self.uid = str(self.lineEdit_uid.text())
            self.nik = str(self.lineEdit_nik.text())
            self.wo = str(self.lineEdit_wo.text())

            if not self.name and not self.fname and not self.phone and \
                    not self.uid and not self.nik and not self.wo:
                raise Local_error("Нет данных для вставки")

            input_check(self.name)
            input_check(self.fname)
            input_check(self.phone)
            input_check(self.uid)
            input_check(self.nik)
            input_check(self.wo)

            insert(g_collection,
                   name=self.name,
                   fname=self.fname,
                   phone=self.phone,
                   uid=self.uid,
                   nik=self.nik,
                   wo=self.wo)
            print("добавил")

        except Local_error as e:
            self.notifier.about(self, " ", str(e))

    def delete(self):
        print("удалить")
        try:
            global g_collection

            self.name = str(self.lineEdit_name.text())
            self.fname = str(self.lineEdit_fname.text())
            self.phone = str(self.lineEdit_phone.text())
            self.uid = str(self.lineEdit_uid.text())
            self.nik = str(self.lineEdit_nik.text())
            self.wo = str(self.lineEdit_wo.text())

            if not self.name and not self.fname and not self.phone and \
                    not self.uid and not self.nik and not self.wo:
                raise Local_error("Нет данных для удаления")

            input_check(self.name)
            input_check(self.fname)
            input_check(self.phone)
            input_check(self.uid)
            input_check(self.nik)
            input_check(self.wo)

            data = {"name": self.name, "fname": self.fname,
                    "phone": self.phone, "uid": self.uid,
                    "nik": self.nik, "wo": self.wo}

            delete(g_collection,
                   name=self.name,
                   fname=self.fname,
                   phone=self.phone,
                   uid=self.uid,
                   nik=self.nik,
                   wo=self.wo)
            print("удалил")

        except Local_error as e:
            self.notifier.about(self, " ", str(e))

    def forward(self):
        try:
            global g_collection
            global g_page_number
            global g_pages_total

            g_page_number += 1

            if g_page_number > g_pages_total:
                g_page_number -= 1
                raise Local_error("Это самая последняя страница")

            page_begin = 100 * g_page_number - 100

            response = find(g_collection,
                            name=self.name,
                            fname=self.fname,
                            phone=self.phone,
                            uid=self.uid,
                            nik=self.nik,
                            wo=self.wo,
                            skip=page_begin,
                            limit=100)

            self.lineEdit_pages_cur.setText(str(g_page_number))

            for row_number, row_value in enumerate(response):
                for item_number, item_value in enumerate(row_value):
                    self.tableWidget.setItem(
                        row_number, item_number, QTableWidgetItem(
                            str(list(row_value.values())[item_number]))
                    )
                    self.tableWidget.horizontalHeaderItem(
                        item_number).setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget.resizeColumnsToContents()
        except Local_error as e:
            self.notifier.about(self, " ", str(e))

    def back(self):
        try:
            global g_collection
            global g_page_number
            global g_pages_total

            g_page_number -= 1

            if g_page_number < 1:
                g_page_number += 1
                raise Local_error("Это самая первая страница")

            page_begin = 100 * g_page_number - 100

            response = find(g_collection,
                            name=self.name,
                            fname=self.fname,
                            phone=self.phone,
                            uid=self.uid,
                            nik=self.nik,
                            wo=self.wo,
                            skip=page_begin,
                            limit=100)

            self.lineEdit_pages_cur.setText(str(g_page_number))

            for row_number, row_value in enumerate(response):
                for item_number, item_value in enumerate(row_value):
                    self.tableWidget.setItem(
                        row_number, item_number, QTableWidgetItem(
                            str(list(row_value.values())[item_number]))
                    )
                    self.tableWidget.horizontalHeaderItem(
                        item_number).setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget.resizeColumnsToContents()
        except Local_error as e:
            self.notifier.about(self, " ", str(e))

    def stop(self):
        global g_active_import
        global g_active_export

        g_active_import = False
        g_active_export = False


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
    global g_collection
    client = MongoClient()
    db = client["db"]
    g_collection = db["collection"]


def insert(collection, _id="", name="", fname="", phone="",
           uid="", nik="", wo="", data=None):
    try:
        if data is None:
            request = {}
            if _id != "":
                request.update({"_id": str(_id)})
            if name != "":
                request.update({"name": str(name)})
            if fname != "":
                request.update({"fname": str(fname)})
            if phone != "":
                request.update({"phone": str(phone)})
            if uid != "":
                request.update({"uid": str(uid)})
            if nik != "":
                request.update({"nik": str(nik)})
            if wo != "":
                request.update({"wo": str(wo)})

            collection.insert_one(request)
        else:
            collection.insert_many(data)
    except errors.InvalidDocument as e:
        raise Local_error(str(e))
    except pymongo.errors.BulkWriteError:
        raise Local_error(
            "В файле не должно быть\nповторяющихся полей '_id'")


def find(collection, _id="", name="", fname="", phone="",
         uid="", nik="", wo="", skip=0, limit=0):
    try:
        request = {}
        if _id != "":
            request.update({"_id": str(_id)})
        if name != "":
            request.update({"name": str(name)})
        if fname != "":
            request.update({"fname": str(fname)})
        if phone != "":
            request.update({"phone": str(phone)})
        if uid != "":
            request.update({"uid": str(uid)})
        if nik != "":
            request.update({"nik": str(nik)})
        if wo != "":
            request.update({"wo": str(wo)})

        c = collection.find(request, skip=skip, limit=limit,
                            allow_partial_results=True)

        data = [i for i in c]
        return data
    except pymongo.errors.OperationFailure as e:
        raise Local_error(str(e))


def replace(collection, _id, data):
    data_pull = find(collection, _id=_id, limit=1)[0]
    data_pull.update(data)

    collection.replace_one({'_id': str(_id)}, data_pull)


def delete(collection, _id="", name="", fname="", phone="",
           uid="", nik="", wo=""):
    try:
        request = {}
        if _id != "":
            request.update({"_id": str(_id)})
        if name != "":
            request.update({"name": str(name)})
        if fname != "":
            request.update({"fname": str(fname)})
        if phone != "":
            request.update({"phone": str(phone)})
        if uid != "":
            request.update({"uid": str(uid)})
        if nik != "":
            request.update({"nik": str(nik)})
        if wo != "":
            request.update({"wo": str(wo)})

        a = collection.delete_one(request)
    except pymongo.errors.OperationFailure as e:
        raise Local_error(str(e))


def import_data(collection, path):
    global g_max_value
    global g_current_value
    global g_active_import
    global headers

    try:
        g_active_import = True
        if not os.path.exists(path):
            raise Local_error("path doesn't exists")

        collection.drop()
        g_max_value = 100
        g_current_value = 1
        with open(path, 'r', encoding="Windows-1251") as f:
            g_max_value = sum(1 for _ in f) - 1

        with open(path, 'r', encoding="Windows-1251") as f:
            f.readline()

            block = 10000
            data = []

            from time import time
            start = time()
            print("начало в ", start)
            g_current_value = 0
            for line in f:
                g_current_value += 1
                if line.isspace() or "|" not in line:
                    continue

                line = line[1:-2].split("|")[:7]
                iter_data = {}
                for i, item in enumerate(line):
                    iter_data.update({headers[i]: str(item)})

                data.append(iter_data)

                if g_current_value % block == 0:
                    data.sort(key=lambda field: int(field['_id']))
                    insert(collection, data=data)

                    data = []

                elif g_current_value >= g_max_value:
                    data.sort(key=lambda field: int(field['_id']))
                    insert(collection, data=data)

                    iter_data = {}
                    data = []

                if not g_active_import:
                    print("останов")
                    break

        g_current_value = 100

        eee = str((time() - start) / 60).split(".")
        print(eee[0] + "." + eee[1][:3] + " min")
    except Local_error as e:
        raise Local_error(str(e))
    finally:
        g_active_import = False


def export_data_master(collection, path, data_in):
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


def gen_new_csv_name():
    path = os.path.join(get_script_dir(), "get_csv_here")
    if not os.path.exists(path):
        os.mkdir(path)
    files = os.listdir(path)
    i = 1
    while f"result{i}.csv" in files:
        i += 1
    return f"result{i}.csv"


def input_check(data):
    if isinstance(data, str):
        if "," in data or "|" in data or "\n" in data:
            raise Local_error(
                f"'{data}' contains an unsupported" +
                "symbol: \n{','; '|'; '\\n'}")
    else:
        raise Local_error(f"'{data}' is not a string")


def main():
    app = QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()


if __name__ == '__main__':
    main()
