import db

if __name__ == "__main__":
    collection = db.init_collection()
    db.insert(collection, {"test1": 123})
