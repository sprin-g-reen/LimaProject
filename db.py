from pymongo import MongoClient
db_url = "mongodb+srv://bot:bot@cluster.grbz9zy.mongodb.net/test"

_db = MongoClient(db_url)["website"]

class db:
    users = _db["users"]
    coupons = _db["coupons"]