from pymongo import MongoClient
conn = MongoClient()
db = conn.zipp
collection = db.stateaddresses
user_input = raw_input()
