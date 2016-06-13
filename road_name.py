from fuzzywuzzy import fuzz
from nltk import *
from pymongo import MongoClient
conn = MongoClient()
db=conn.zipprx
text=raw_input().split(",")
test=[]
new=[]
[new.append(x[u'road_name']) for x in db.road_name.find()]
print len(new)
# count=0
arr=["road","line","way","marg","pass","street","drive","putih","gali","veedhi","galli","path","lane","khand","cross","avenue","square","walk"]
for i in range(len(arr)):
    for j in range(len(text)):
        if arr[i] in text[j]:
            test.append(text[j])
        elif str(arr[i]).capitalize() in text[j]:
            test.append(text[j])
print "Given Road Name:"
for x in range(len(test)):
    print test[x]
for j in range(len(new)):
    print new[j]

print test
max=0
result=None
for i in range(len(test)):
    for j in range(len(new)):
        if fuzz.ratio(test[i],new[j])>max:
            result=new[j]
            max=fuzz.ratio(test[i],new[j])
            name=test[i]
if max>90:
    print "Result:",test[i]
else:
    print "Did you mean:",result