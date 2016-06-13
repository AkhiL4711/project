from pymongo import *
conn = MongoClient()
db = conn.tut
for obj in db.tut.find({'num':{'$gt':1}}):
    print obj
print list(db.tut.find().sort([("author",1)]))


