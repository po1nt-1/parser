import inspect
import json
import os
import sys
from pprint import pprint

import pymongo
from bson import errors
from bson.objectid import ObjectId
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


def init_collection(collection_name):
    client = MongoClient()
    collection = client["db"][collection_name]

    return collection


def set(collection, data):
    try:
        if not isinstance(data, list):
            collection.insert_one(data)
        else:
            collection.insert_many(data)
    except errors.InvalidDocument as e:
        raise local_error(str(e))


def get(collection, dictry={}, skip=0, limit=0):
    try:
        request = collection.find(dictry).skip(skip).limit(limit)
        data = [i for i in request]
    except pymongo.errors.OperationFailure as e:
        raise local_error(str(e))
    return data


def replace(collection, _id, data):
    collection.replace_one({'_id': ObjectId(_id)}, data)


def delete(collection, data):
    collection.TODO(data)


if __name__ == "__main__":
    try:
        collection = init_collection("collection")
        # set(collection, {"hard": [-1, -2, -3, {"oh": "my", "well": "done"}]})
        # pprint(get(collection))

        replace(collection, "5f6df8e1099565cb1542f672", {"ey": "value"})

    except local_error as e:
        print("Error: " + str(e))
