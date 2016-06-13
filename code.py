    import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

query = raw_input("How can we help you...?")
tokend_query = word_tokenize(query)
pos_query = pos_tag(tokend_query)
new_query = []

no_of_words = len(tokend_query)
for i in range(no_of_words):
    if pos_query[i][1] == "NNP":
        new_query.append(pos_query[i][0])
new_query2=[tup[0] for tup in pos_query if tup[1]=="NN"]
print new_query
print new_query2


from pymongo import MongoClient
client = MongoClient()  #Making a connection with mongiClient

db = client.zipprx  #getting a database
collection = db.address #getting a collection from the database

result = []
# count = 0


#Manupulations on the database


addr=[[obj.setdefault(u'address'," "),obj.setdefault(u'title'," "),obj.setdefault(u'zippr'," ")] for obj in db.address.find()]
print len(addr)
print (addr[0][0][u'sublocality'])

# for j in range(0,len(new_query)):
#     for i in range(0,len(addr)):
#         if(addr[i][0]!=" " and addr[i][0]!=None):
#             try:
#                 if (new_query[j]) in addr[i][0][u'sublocality']:
#                     result.append(addr[i])
#             except KeyError:
#                 addr[i][0][u'sublocality']=None
# print result
print (addr[1][0].keys())
for j in range(len(addr)):
    for i in range(len(new_query)):
        if addr[j][0] != " " and addr[j][0] != None:
            if u'locality' in addr[j][0].keys():
                if new_query[i] in addr[j][0][u'locality']: #.setdefault('locality', " ")
                    result.append(addr[j])
print result

result_final=[]
for j in range(0,len(result)):
    for i in range(0,len(new_query2)):
        if(result[j][1]!=None):
            if(new_query2[i] in result[j][1]):
                result_final.append(addr[j][2])
print result_final










