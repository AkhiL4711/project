from pymongo import MongoClient, GEOSPHERE
import pprint
conn = MongoClient()
db = conn.zipprx
for obj in db.address.find({"zippr":"ZPPR2727"}):
    #print obj
    print obj[u'title']
    lat=obj[u'location'][u'coordinates'][1]
    lon=obj[u'location'][u'coordinates'][0]
default=" "
l=[obj.setdefault(u'title',default) for obj in db.address.find({ "location": { "$nearSphere": { "$geometry": { "type": "Point", "coordinates": [ lon , lat ] }, "$maxDistance": 1000 } } })]
print l
