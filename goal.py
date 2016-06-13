import re, collections

def words(text):
    return re.findall('[a-z]+', text.lower())

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(words(file('D:\Akhil\check.txt').read()))
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
    s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in s if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in s for c in alphabet if b]
    inserts    = [a + c + b     for a, b in s for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words):
    return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or    known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#accessing the excel file


from pymongo import MongoClient
conn = MongoClient()
db = conn.zipp
collection = db.stateaddresses
print db.stateaddresses.find_one()

countries = [obj[u'CountryName'] for obj in db.stateaddresses.find()]

India_States = [obj[u'StateName'] for obj in db.stateaddresses.find()]

Districts = [obj[u'DistrictName'] for obj in db.stateaddresses.find()]

Sub_Districts = [obj[u'SubDistrictName'] for obj in db.stateaddresses.find()]


address = raw_input("Enter address... \n")

# import regex
# pin=regex.search( r"\b\d{5}\b",address )
# print pin
tokend_address = list(address.split())


for i in range(len(tokend_address)):
    tokend_address[i] = correct(tokend_address[i])   ##--correcting the wrongly spelled words
    tokend_address[i] = tokend_address[i][:1].upper()+tokend_address[i][1:]

print tokend_address

main_address = {}

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#Country and State

dum = []
Country = " "
for j in range(len(tokend_address)):
    if tokend_address[j] in countries:
        Country = tokend_address[j]
        main_address["Country"] = tokend_address[j]
    else:
        for k in range(len(India_States)):
            if tokend_address[j] in India_States[k] and tokend_address[j] not in dum:
                dum.append(tokend_address[j])

if len(dum) > 1:
    State = " "
    for m in range(len(dum)):
        State = State + dum[m] + " "
        tokend_address.remove(dum[m])
    main_address["State"] = State

elif len(dum) == 1:
    State = dum[0]
    tokend_address.remove(dum[0])
    main_address["State"] = State

tokend_address.remove(Country)

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#Districts

dumm = []
for j in range(len(tokend_address)):
   for k in range(len(Districts)):
        if tokend_address[j] in Districts[k] and tokend_address[j] not in dumm:
            dumm.append(tokend_address[j])

if len(dumm) > 1:
    District = " "
    for m in range(len(dumm)):
        District = District + dumm[m] + " "
        tokend_address.remove(dumm[m])
    main_address["District"] = District

elif len(dumm) == 1:
    District = dumm[0]
    tokend_address.remove(dumm[0])
    main_address["District"] = District

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#Sub_Districts

dummy = []
for j in range(len(tokend_address)):
   for k in range(len(Sub_Districts)):
        if tokend_address[j] in Sub_Districts[k] and tokend_address[j] not in dummy:
            dummy.append(tokend_address[j])

if len(dummy) > 1:
    Sub_District = " "
    for m in range(len(dummy)):
        Sub_District = Sub_District + dummy[m] + " "
        tokend_address.remove(dummy[m])
    main_address["Sub_District"] = Sub_District

elif len(dummy) == 1:
    Sub_District = dummy[0]
    tokend_address.remove(dummy[0])
    main_address["Sub_District"] = Sub_District


print main_address
