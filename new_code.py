from fuzzywuzzy import fuzz
import json
from pymongo import MongoClient
conn = MongoClient()
db=conn.zipprx
# coll=db.address
# pin_code="500013"
text=raw_input()
pin=text.split()
pin_code=None
for i in range(len(pin)):
    if pin[i].isdigit() and len(pin[i])==6:
        pin_code=pin[i]
if pin_code is not None:
    text.replace(pin_code,"")
print text
data=text.split(",")

# doc=db.address.find_one()
sublocality=[x[u'sublocality'] for x in db.sublocality.find()]
locality=[x[u'locality'] for x in db.locality.find()]
landmark=[x[u'landmark'] for x in db.landmark.find()]


# locality=
# landmark=
# if pin_code is None:
#     addr=[[obj.setdefault(u'address_v3'," "),obj.setdefault(u'title'," "),obj.setdefault(u'zippr'," ")] for obj in db.address.find()]
#     # {u'address': {u'dumps': None}}
# else:
#     addr=[[obj.setdefault(u'address_v3'," "),obj.setdefault(u'title'," "),obj.setdefault(u'zippr'," ")] for obj in db.address.find({u'address.postal_code': pin_code})]
# # print len(addr)
# print (addr[0][0][u'sublocality'])
# print len(addr)
# s=json.loads(sublocality)
# print [obj[u'sublocality'] for obj in s]

print pin_code
# for i in range(len(addr)):
#     if
#========================================================================================================================
#========================================================================================================================
maximum = 0
print data
user_locality=None
user_sublocality=None
user_landmark=None
for x in locality:
    if fuzz.partial_ratio(data[-1],x)>maximum:
        user_locality=x
        maximum = fuzz.partial_ratio(data[-1],x)
if maximum > 90:
    print data[-1]
    del data[-1]

maximum = 0
for x in sublocality:
    if fuzz.partial_ratio(data[-1],x)>maximum:
        user_sublocality=x
        maximum = fuzz.partial_ratio(data[-1],x)
if maximum > 90:
    print data[-1]
    del data[-1]

maximum = 0
for x in landmark:
    if fuzz.partial_ratio(data[-1],x)>maximum:
        user_landmark=x
        maximum = fuzz.partial_ratio(data[-1],x)
if maximum > 90:
    print data[-1]
    del data[-1]
if user_locality is not None:
    print "Locality:",user_locality
# elif user_sublocality is not None:
#     user_locality=user_sublocality.split(",")[-1]
if user_landmark is not None:
    user_landmark=user_landmark.split(",")[0]
    print "Landmark:",user_landmark
if user_sublocality is not None:
    print "Sublocality:",user_sublocality
print data
# Near YSR Statue,100 feet road,Madhapur
#======================================================================================================================

if user_landmark is not None:
    search=[x.setdefault(u'title',None) for x in db.address.find({u'address_v3.landmark': user_landmark})]
elif user_sublocality is not None:
    search=[x.setdefault(u'title',None) for x in db.address.find({u'address_v3.sublocality':user_sublocality})]
elif user_locality is not None:
    search=[x.setdefault(u'title',None) for x in db.address.find({u'address_v3.locality':user_locality})]
else:
    search=[x.setdefault(u'title',None) for x in db.address.find()]
#=======================================================================================================================
print len(search)
# for x in search:
#     try:
#
#
