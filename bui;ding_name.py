from pymongo import MongoClient
conn = MongoClient()
db=conn.zipprx
new=[]
[new.append(x[u'building_name']) for x in db.building_name.find()]
names=["tower","enclave","apt","apartment","nivas","building","bhawan","bhavan","niwas",""]
for i in range(len(new)):
    print new[i]
print len(new)
# regex--'![0-9/-]+!'