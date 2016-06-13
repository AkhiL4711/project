from pymongo import MongoClient, GEOSPHERE
import pprint
conn = MongoClient()
db = conn.zipprx
for obj in db.address.find({"zippr":"JEQK8240"}):
    print obj
#     lat=obj[u'location'][u'coordinates'][1]
#     lon=obj[u'location'][u'coordinates'][0]
# print [obj[u'zippr'] for obj in db.address.find({ "location": { "$nearSphere": { "$geometry": { "type": "Point", "coordinates": [ lon , lat ] }, "$maxDistance": 1 } } })]
for j in range(len(addr)):
    for i in range(len(locality)):
        if addr[j][0] != " " and addr[j][0] != None:
            if "u'locality'" in addr[j][0]:
                if locality[i] in addr[j][0][u'locality']: #.setdefault('locality', " ")
                    pre_result.append(addr[j][2])