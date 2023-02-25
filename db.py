from pymongo import MongoClient
db_url = "mongodb://localhost:27017"

_db = MongoClient(db_url)["website"]

class db:
    users = _db["users"]