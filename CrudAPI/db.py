from pymongo import MongoClient

def connect_db():
    client = MongoClient('mongodb://localhost:27017')
    return client