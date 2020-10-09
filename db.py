import inspect
import json
import os
import sys

import pymongo
from bson import errors
from pymongo import MongoClient


class local_error(Exception):
    pass


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
    if not os.path.exists(path):
        raise local_error("path doesn't exists")

    collection.drop()

    headers = ['_id', 'name', 'fname', 'phone', 'uid', 'nik', 'wo']
    with open(path, 'r', encoding="utf-8", errors="ignore") as f:
        data_len = sum(1 for _ in f) - 1

    with open(path, 'r', encoding="utf-8", errors="ignore") as f:
        f.readline()
        counter = 0
        block = 100000
        data = []

        from time import time
        start = time()

        for line in f:
            counter += 1
            line = line[1:-2].split("|")[:7]
            iter_data = {}
            for i, item in enumerate(line):
                iter_data.update({headers[i]: str(item)})

            data.append(iter_data)

            if counter % block == 0:
                insert(collection, data)
                data = []
                print(time() - start)

            elif counter == data_len:
                insert(collection, data)
                iter_data.clear()
                data.clear()
                data = []


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

    except local_error as e:
        print("Error: " + str(e))


if __name__ == "__main__":
    main()
