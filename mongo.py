from pymongo import MongoClient
conn = MongoClient()
db=conn.zipprx
# sublocality=[]
building_name=[]
# landmark=[]
try:
    for obj in db.address.find():
        if u'address_v3' in obj:
            if u'user_buildingname' in obj[u'address_v3']:
                if obj[u'address_v3'][u'user_buildingname']!="":
                    building_name.append(obj[u'address_v3'][u'user_buildingname'])
except TypeError:
    print None
building_name=list(set(building_name))
conn.close()
conn_new=MongoClient()
db_new=conn_new.zipprx
coll_new=db.building_name
for x in building_name:
    db.building_name.insert_one({
        "building_name" : x
    })
# l=[]
# [l.append(x[u'building_name']) for x in db.building_name.find()]
# print len(l)
# print l