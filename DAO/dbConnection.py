from pymongo import MongoClient

connection = MongoClient("mongodb://127.0.0.1:27017")
db = connection.pyDB

def getCollectionNames():
    collection = db['testCollection']
    cursor = collection.find({})
    titles = []
    for doc in cursor:
        titles.append(doc['title'])

    return titles