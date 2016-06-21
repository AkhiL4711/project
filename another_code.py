from pymongo import MongoClient
from fuzzywuzzy import fuzz
from nltk import word_tokenize
from nltk import pos_tag
import unicodedata
import xlrd
conn = MongoClient()
db=conn.zip
#vijayawada benz circle andhra pradesh india near pragathi apartments
# import re, collections
#
# def words(text): return re.findall('[a-z]+', text.lower())
#
# def train(features):
#     model = collections.defaultdict(lambda: 1)
#     for f in features:
#         model[f] += 1
#     return model
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# NWORDS = train(words(file('big.txt').read()))
#
#
# def edits1(word):
#    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
#    deletes    = [a + b[1:] for a, b in splits if b]
#    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
#    replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
#    inserts    = [a + c + b     for a, b in splits for c in alphabet]
#    return set(deletes + transposes + replaces + inserts)
#
# def known_edits2(word):
#     return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)
#
# def known(words): return set(w for w in words if w in NWORDS)
#
# def correct(word):
#     candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
#     return max(candidates, key=NWORDS.get)

address = raw_input("Enter address... \n")

tokend_address=address.split()

path = "C:\Users\zippr\Desktop\India_State_District_SubDistrict_LocationFile_FullData.xls"

book = xlrd.open_workbook(path)

first_sheet = book.sheet_by_index(0)

countries = first_sheet.col_values(0)
del countries[0]

India_States = first_sheet.col_values(1)
del India_States[0]

Districts = first_sheet.col_values(2)
del Districts[0]

Sub_Districts = first_sheet.col_values(3)
del Sub_Districts[0]



for i in range(len(tokend_address)):
    tokend_address[i] = tokend_address[i].capitalize()

main_address = {}

Pincode = ""
for i in range(len(tokend_address)):
    if tokend_address[i].isdigit() and len(tokend_address[i])== 6:
        Pincode = tokend_address[i]
        main_address["Pincode"] = int(tokend_address[i])
        tokend_address.remove(tokend_address[i])
        break

# def sublist(a, b):
#     seq = iter(b)
#     try:
#         for y in a:
#             while seq.next() != y:
#                 pass
#         else:
#             return True
#     except StopIteration:
#         pass
#     return False
def text2int(textnum, numwords={}):
    start=0
    if not numwords:
        units = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']


        tens = ["", "", 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        scales = ['Hundred', 'Thousand', 'Million', 'Billion', 'Trillion']

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):  numwords[word] = (1, idx)
        for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    ordinal_words = {'First':1, 'Second':2, 'Third':3, 'Fifth':5, 'Eighth':8, 'Ninth':9, 'Twelfth':12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    textnum = textnum.replace('-', ' ')

    current = result = 0
    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if word not in numwords:
                if start==0:
                    continue

            scale, increment = numwords[word]
            start=1
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current


def tex(x):
    numwords = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred', 'Thousand', 'Million', 'Billion', 'Trillion', 'And']



    ordinal_words = ['First', 'Second', 'Third', 'Fifth', 'Eighth', 'Ninth', 'Twelfth']
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    if x not in ordinal_words:
        for ending, replacement in ordinal_endings:
            if x.endswith(ending):
                x = "%s%s" % (x[:-len(ending)], replacement)

        if x in numwords:
            return True
    else:
        return True
    return False

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def hasHyphen(inputString):
    return any(char=="-" for char in inputString)

def hasSlash(inputString):
    return any(char=="/" for char in inputString)



def sublist(a, b):
    if not a:
        return True
    for k in range(len(b)):
        if fuzz.ratio(a[0],b[k])>80:
            return sublist(a[1:], b[k+1:])
    return False

# India_States_set = list(set(India_States))
# State = ''
# for k in range(len(India_States_set)):
#     first = True
#     fake_a = []
#     fake_c = []
#     prev = 0
#     State = State + ""
#     dummy = []
#     if India_States_set[k] != None and India_States_set[k]!= '' and India_States_set[k] != " ":
#         dum = list(India_States_set[k].split())
#         for a in range(len(dum)):
#             title = unicodedata.normalize('NFKD', dum[a]).encode('ascii', 'ignore')
#             dummy.append(title)
#         there = sublist(dummy, tokend_address)
#         if there:
#             for j in range(len(tokend_address)):
#                 for i in range(len(dummy)):
#                     if fuzz.ratio(dummy[i],tokend_address[j])>85:
#                         tokend_address[j]=dummy[i]
#             if len(dummy) == 1:
#                 State = State +India_States_set[k]
#             else:
#                 for i in range(len(dummy)):
#                     if first:
#                         indexes = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
#                         for l in range(len(indexes)):
#                             fake_a.append(indexes[l])
#                         first = False
#                     else:
#                         fake_b = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
#                         for j in range(len(fake_b)):
#                             if fake_b[j]-1 in fake_a:
#                                 fake_c.append(fake_b[j])
#                         if len(fake_c) == 1:
#                             State = State + India_States_set[k]
#                         else:
#                             fake_a = fake_c
#
#
# main_address['State'] = State
# to_be_rmvd = list(State.split())
# for j in range(len(to_be_rmvd)):
#     tokend_address.remove(to_be_rmvd[j])
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #gandhi nagar namburi vari street andhra pradesh krishna pedana 509001
#
#
#
#
#
#
#
#
# Districts_set = list(set(Districts))
# District = ''
# for k in range(len(Districts_set)):
#     first = True
#     fake_a = []
#     fake_c = []
#     prev = 0
#     District = District + ""
#     dummy = []
#     if Districts_set[k] != None and Districts_set[k]!= '' and Districts_set[k] != " ":
#         dum = list(Districts_set[k].split())
#         for a in range(len(dum)):
#             title = unicodedata.normalize('NFKD', dum[a]).encode('ascii', 'ignore')
#             dummy.append(title)
#         there = sublist(dummy, tokend_address)
#         if there:
#             for j in range(len(tokend_address)):
#                 for i in range(len(dummy)):
#                     if fuzz.ratio(dummy[i], tokend_address[j]) > 85:
#                         tokend_address[j] = dummy[i]
#             if len(dummy) == 1:
#                 District = District +Districts_set[k]
#             else:
#                 for i in range(len(dummy)):
#                     if first:
#                         indexes = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
#                         for l in range(len(indexes)):
#                             fake_a.append(indexes[l])
#                         first = False
#                     else:
#                         fake_b = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
#                         for j in range(len(fake_b)):
#                             if fake_b[j]-1 in fake_a:
#                                 fake_c.append(fake_b[j])
#                         if len(fake_c) == 1:
#                             District = District + Districts_set[k]
#                         else:
#                             fake_a = fake_c
#
#
# main_address['District'] = District
# to_be_rmvd = list(District.split())
# for j in range(len(to_be_rmvd)):
#     tokend_address.remove(to_be_rmvd[j])
#
#
# District_indexes = [int(i) for i, x in enumerate(Districts) if x == District]
#
# g = District_indexes[0]
# h = District_indexes[-1]
#
#
#
# Sub_Districts_set = list(Sub_Districts[g:h+1])
# Sub_District = ''
# for k in range(len(Sub_Districts_set)):
#     first = True
#     fake_a = []
#     fake_c = []
#     prev = 0
#     Sub_District = Sub_District + ""
#     dummy = []
#     if Sub_Districts_set[k] != None and Sub_Districts_set[k]!= '' and Sub_Districts_set[k] != " ":
#         dum = list(Sub_Districts_set[k].split())
#         for a in range(len(dum)):
#             title = unicodedata.normalize('NFKD', dum[a]).encode('ascii', 'ignore')
#             dummy.append(title)
#         there = sublist(dummy, tokend_address)
#         if there:
#             for j in range(len(tokend_address)):
#                 for i in range(len(dummy)):
#                     if fuzz.ratio(dummy[i], tokend_address[j]) > 85:
#                         tokend_address[j] = dummy[i]
#             if len(dummy) == 1:
#                 Sub_District = Sub_District +Sub_Districts_set[k]
#             else:
#                 for i in range(len(dummy)):
#                     if first:
#                         indexes = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
#                         for l in range(len(indexes)):
#                             fake_a.append(indexes[l])
#                         first = False
#                     else:
#                         fake_b = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
#                         for j in range(len(fake_b)):
#                             if fake_b[j]-1 in fake_a:
#                                 fake_c.append(fake_b[j])
#                         if len(fake_c) == 1:
#                             Sub_District = Sub_District + Sub_Districts_set[k]
#                         else:
#                             fake_a = fake_c
#
#
# main_address['City'] = Sub_District
# to_be_rmvd = list(Sub_District.split())
# if len(to_be_rmvd) > 0:
#     for j in range(len(to_be_rmvd)):
#         tokend_address.remove(to_be_rmvd[j])




Localities = [x[u'locality'] for x in db.locality.find()]

Sub_Localities = [x[u'sublocality'] for x in db.sublocality.find()]

Landmarks = [x[u'landmark'] for x in db.landmark.find()]

Roadnames = [x[u'road_name'] for x in db.road_name.find()]

Buildings = [x[u'building_name'] for x in db.building_name.find()]



Localities_set = list(set(Localities))
Locality = ''
for k in range(len(Localities_set)):
    first = True
    fake_a = []
    fake_c = []
    prev = 0
    Locality = Locality + ""
    dummy = []
    if Localities_set[k] != None and Localities_set[k]!= '' and Localities_set[k] != " ":
        dum = list(Localities_set[k].split())
        for a in range(len(dum)):
            title = unicodedata.normalize('NFKD', dum[a]).encode('ascii', 'ignore')
            dummy.append(title)
        there = sublist(dummy, tokend_address)
        if there:
            for j in range(len(tokend_address)):
                for i in range(len(dummy)):
                    if fuzz.ratio(dummy[i], tokend_address[j]) > 85:
                        tokend_address[j] = dummy[i]
            if len(dummy) == 1:
                Locality = dummy[0]
            else:
                for i in range(len(dummy)):
                    if first:
                        indexes = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
                        for l in range(len(indexes)):
                            fake_a.append(indexes[l])
                        first = False
                    else:
                        fake_b = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
                        for j in range(len(fake_b)):
                            if fake_b[j]-1 in fake_a:
                                fake_c.append(fake_b[j])
                        if len(fake_c) == 1:
                            Locality = ''
                            Locality = Locality + Localities_set[k]
                        else:
                            fake_a = fake_c

main_address['Locality'] = Locality
to_be_rmvd = list(Locality.split())
if len(to_be_rmvd) > 0:
    for j in range(len(to_be_rmvd)):
        tokend_address.remove(to_be_rmvd[j])






Sub_Localities_set = list(set(Sub_Localities))
Sub_Locality = ''
for k in range(len(Sub_Localities_set)):
    first = True
    fake_a = []
    fake_c = []
    prev = 0
    Sub_Locality = Sub_Locality + ""
    dummy = []
    if Sub_Localities_set[k] != None and Sub_Localities_set[k]!= '' and Sub_Localities_set[k] != " ":
        dum = list(Sub_Localities_set[k].split())
        for a in range(len(dum)):
            title = unicodedata.normalize('NFKD', dum[a]).encode('ascii', 'ignore')
            dummy.append(title)
        there = sublist(dummy, tokend_address)
        if there:
            for j in range(len(tokend_address)):
                for i in range(len(dummy)):
                    if fuzz.ratio(dummy[i], tokend_address[j]) > 85:
                        tokend_address[j] = dummy[i]
            if len(dummy) == 1:
                Sub_Locality = dummy[0]
            else:
                for i in range(len(dummy)):
                    if first:
                        indexes = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
                        for l in range(len(indexes)):
                            fake_a.append(indexes[l])
                        first = False
                    else:
                        fake_b = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
                        for j in range(len(fake_b)):
                            if fake_b[j]-1 in fake_a:
                                fake_c.append(fake_b[j])
                        if len(fake_c) == 1:
                            Sub_Locality = ''
                            Sub_Locality = Sub_Locality + Sub_Localities_set[k]
                        else:
                            fake_a = fake_c

main_address['Sub_Locality'] = Sub_Locality
to_be_rmvd = list(Sub_Locality.split())
if len(to_be_rmvd) > 0:
    for j in range(len(to_be_rmvd)):
        tokend_address.remove(to_be_rmvd[j])




print "hhgjkkhnkdnhkxdknbdhgkndjhgkdjfhjbngkjrhgkjfxdnghdkjghdngkjhesrjkghjk"


Landmarks_set = list(set(Landmarks))
Landmark = ''
for k in range(len(Landmarks_set)):
    first = True
    fake_a = []
    fake_c = []
    prev = 0
    Landmark = Landmark + ""
    dummy = []
    if Landmarks_set[k] != None and Landmarks_set[k]!= '' and Landmarks_set[k] != " ":
        dum = list(Landmarks_set[k].split())
        for a in range(len(dum)):
            title = unicodedata.normalize('NFKD', dum[a]).encode('ascii', 'ignore')
            dummy.append(title)
        there = sublist(dummy, tokend_address)
        if there:
            for j in range(len(tokend_address)):
                for i in range(len(dummy)):
                    if fuzz.ratio(dummy[i], tokend_address[j]) > 85:
                        tokend_address[j] = dummy[i]
            if len(dummy) == 1:
                Landmark = dummy[0]
            else:
                for i in range(len(dummy)):
                    if first:
                        indexes = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
                        for l in range(len(indexes)):
                            fake_a.append(indexes[l])
                        first = False
                    else:
                        fake_b = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
                        for j in range(len(fake_b)):
                            if fake_b[j]-1 in fake_a:
                                fake_c.append(fake_b[j])
                        if len(fake_c) == 1:
                            Landmark = ''
                            Landmark = Landmark + Landmarks_set[k]
                        else:
                            fake_a = fake_c

main_address['Landmark'] = Landmark
to_be_rmvd = list(Landmark.split())
if len(to_be_rmvd) > 0:
    for j in range(len(to_be_rmvd)):
        tokend_address.remove(to_be_rmvd[j])


Roadnames_set = list(set(Roadnames))
Roadname = ''
for k in range(len(Roadnames_set)):
    first = True
    fake_a = []
    fake_c = []
    prev = 0
    Roadname = Roadname + ""
    dummy = []
    if Roadnames_set[k] != None and Roadnames_set[k]!= '' and Roadnames_set[k] != " ":
        dum = list(Roadnames_set[k].split())
        for a in range(len(dum)):
            title = unicodedata.normalize('NFKD', dum[a]).encode('ascii', 'ignore')
            dummy.append(title)
        there = sublist(dummy, tokend_address)
        if there:
            for j in range(len(tokend_address)):
                for i in range(len(dummy)):
                    if fuzz.ratio(dummy[i], tokend_address[j]) > 85:
                        tokend_address[j] = dummy[i]
            if len(dummy) == 1:
                Roadname = dummy[0]
            else:
                for i in range(len(dummy)):
                    if first:
                        indexes = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
                        for l in range(len(indexes)):
                            fake_a.append(indexes[l])
                        first = False
                    else:
                        fake_b = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
                        for j in range(len(fake_b)):
                            if fake_b[j]-1 in fake_a:
                                fake_c.append(fake_b[j])
                        if len(fake_c) == 1:
                            Roadname = ''
                            Roadname = Roadname + Roadnames_set[k]
                        else:
                            fake_a = fake_c

main_address['Roadname'] = Roadname
to_be_rmvd = list(Roadname.split())
if len(to_be_rmvd) > 0:
    for j in range(len(to_be_rmvd)):
        tokend_address.remove(to_be_rmvd[j])




Buildings_set = list(set(Buildings))
Building = ''
for k in range(len(Buildings_set)):
    first = True
    fake_a = []
    fake_c = []
    prev = 0
    Building = Building + ""
    dummy = []
    if Buildings_set[k] != None and Buildings_set[k]!= '' and Buildings_set[k] != " ":
        dum = list(Buildings_set[k].split())
        for a in range(len(dum)):
            title = unicodedata.normalize('NFKD', dum[a]).encode('ascii', 'ignore')
            dummy.append(title)
        there = sublist(dummy, tokend_address)
        if there:
            for j in range(len(tokend_address)):
                for i in range(len(dummy)):
                    if fuzz.ratio(dummy[i], tokend_address[j]) > 85:
                        tokend_address[j] = dummy[i]
            if len(dummy) == 1:
                Building = dummy[0]
            else:
                for i in range(len(dummy)):
                    if first:
                        indexes = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
                        for l in range(len(indexes)):
                            fake_a.append(indexes[l])
                        first = False
                    else:
                        fake_b = [t for t, x in enumerate(tokend_address) if x == dummy[i]]
                        for j in range(len(fake_b)):
                            if fake_b[j]-1 in fake_a:
                                fake_c.append(fake_b[j])
                        if len(fake_c) == 1:
                            Building = ''
                            Building = Building + Buildings_set[k]
                        else:
                            fake_a = fake_c

main_address['Building'] = Building
to_be_rmvd = list(Building.split())
if len(to_be_rmvd) > 0:
    for j in range(len(to_be_rmvd)):
        tokend_address.remove(to_be_rmvd[j])

print tokend_address
print main_address

#==========================================================================================================================


# Building
# Roadname
# Landmark
# Sub_Locality
# Locality
# City
# District
# State

#=========================================================================================================================

res=[]
ans=[]
x=u'address_v3'
if main_address['Building']!='':
    x+=u'.user_buildingname'
    z=main_address['Building']
elif main_address['Roadname']!='':
    x+=u'.road_name'
    y=main_address['Roadname']
elif main_address['Landmark']!='':
    x+=u'.landmark'
    y = main_address['Landmark']
elif main_address['Sub_Locality']!='':
    x+=u'.sublocality'
    y=main_address['Sub_Locality']
elif main_address['Locality']!='':
    x+=u'.locality'
    y=main_address['Locality']
if x is None:
    print "Enter a valid address"
else:
    print x
    print y
    try:
        for obj in db.address.find({x:y}):
            if u'address_v3' in obj:
                if u'user_buildingname' in obj[u'address_v3']:
                    if obj[u'address_v3'][u'user_buildingname']!="":
                        res.append(obj[u'address_v3'][u'user_buildingname'])
            ans.append(obj[u'zippr'])
    except TypeError:
        print None
res=list(set(res))
for i in res:
    print i
for j in ans:
    print j

#=======================================================================================================================
final=tokend_address
user_aptnum=None
# for i in range(len(final)):
#     if ("num" in final[i] or "No" in final[i] or "no" in final[i] or "Num" in final[i]) and hasNumbers(final[i]):
#         if "d" in final[i] or "D" in final[i] or "F" in final[i] or "f" in final[i]:
#             user_aptnum.append(final[i])
#             del final[i]
#             break
#         elif "d" in final[i - 1] or "D" in final[i - 1] or "F" in final[i - 1] or "f" in final[i - 1]:
#             if len(final) > 1:
#                 user_aptnum.append(final[i - 1])
#                 user_aptnum.append(final[i])
#                 del final[i]
#                 del final[i - 1]
#                 break
#     elif i<=len(final)-2:
#         if ("num" in final[i] or "No" in final[i] or "no" in final[i] or "Num" in final[i]) and hasNumbers(final[i+1]):
#             if "d" in final[i - 1] or "D" in final[i - 1] or "F" in final[i - 1] or "f" in final[i - 1]:
#                 user_aptnum.append(final[i - 1])
#                 user_aptnum.append(final[i])
#                 user_aptnum.append(final[i + 1])
#                 del final[i+1]
#                 del final[i]
#                 del final[i - 1]
#                 break
#             elif "d" in final[i] or "D" in final[i] or "F" in final[i] or "f" in final[i]:
#                 user_aptnum.append(final[i])
#                 user_aptnum.append(final[i+1])
#                 del final[i+1]
#                 del final[i]
#                 break
# for x in user_aptnum:
#     if not hasNumbers(x):
#         user_aptnum.remove(x)
for x in final:
    if hasNumbers(x) and (hasHyphen(x) or hasSlash(x)):
        user_aptnum=x
d=0
if user_aptnum is not None:
    for k in user_aptnum:
       if not k.isdigit():
           d+=1
       else:
           break
    tokend_address.remove(user_aptnum)
    main_address['user_aptnum']=user_aptnum[d:]
print main_address
#=========================================================================================================================

names=["tower","enclave","apt","apartment","nivas","building","bhawan","bhavan","niwas","villa","hospital","school","office","center","nilayam","hotel","product","diagnostic","enterprise",
"dispensary","clinic","scan","technolog","sadan","shop","complex","work","restautant","mansion","mess","medic","residen","plaza","hostel","home","nilyam","care","bar","centre","class","travel","niwas","hub","trader","point"
,"college","corporation","arts","pharmac","institute","temple","land"]

floor=tokend_address
f=[]
for i in range(len(floor)):
    if "Floor" in floor[i]:
        print i
        if tex(floor[i-1]):
            print floor[i-1]
            j=i-1
            y=[]
            while tex(floor[j]) and j>=0:
                y.append(floor[j])
                print floor[j]
                j-=1
            y.reverse()
            f=text2int(" ".join(y))
        elif i<=(len(floor)-2) and tex(floor[i + 1]):
            f = text2int(floor[i + 1:])
        elif i<=(len(floor)-3) and tex(floor[i+2]) and "N" in floor[i+1]:
            f=text2int(floor[i+2:])
        elif hasNumbers(floor[i]):
            f=floor[i]
        elif i<=(len(floor)-2) and hasNumbers(floor[i+1]):
            f=floor[i+1]
        elif hasNumbers(floor[i-1]):
            f=floor[i-1]
        elif i<=(len(floor)-3) and hasNumbers(floor[i+2]):
            f=floor[i+2]
r=[]
if type(f)!=int:
    for x in f:
        if x.isdigit():
            r.append(x)
else:
    r.append(str(f))
main_address["Floor_num"]="".join(r)
print main_address

#=========================================================================================================================
