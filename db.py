import inspect
import json
import os
import sys

import pymongo
from bson import errors
from pymongo import MongoClient
from PySide2.QtCore import QThread

from main import Transfer_to_main

g_path_to_csv = ""

g_max_value = 1
g_current_value = 0

helper = Transfer_to_main()


class Transfer_to_db():
    def teleport(self, path):
        global g_path_to_csv
        g_path_to_csv = path


class WorkerThread(QThread):
    def __init__(self, parent=None):
        super(WorkerThread, self).__init__(parent)

    def run(self):
        collection = init_collection()
        import_data(collection, g_path_to_csv)

        return


class local_error(Exception):
    pass


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

    global helper

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

        helper.teleport(0, g_max_value)

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

                helper.teleport(g_current_value, g_max_value)

            elif g_current_value >= g_max_value:
                data.sort(key=lambda field: field['_id'])
                insert(collection, data)

                iter_data.clear()
                data.clear()
                data = []

    helper.teleport(g_current_value, g_max_value)
    eee = str((time() - start) / 60).split(".")
    print(eee[0] + "." + eee[1][:3] + " min")


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
    try:
        collection = init_collection()
        import_data(collection, os.path.join(get_script_dir(),
                                             "test_small_data.txt"))
        # "little_data.txt"))

    except local_error as e:
        print("Error: " + str(e))


if __name__ == "__main__":
    main()
