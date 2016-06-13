from pymongo import MongoClient, GEOSPHERE
conn = MongoClient()
db = conn.zipprx
db.address.create_index([("location", GEOSPHERE)])