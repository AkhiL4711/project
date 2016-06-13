# import xlrd
#
# path = "D:\Study\Project\New folder\data1.xls"
#
# book = xlrd.open_workbook(path)
#
# first_sheet = book.sheet_by_index(0)
from pymongo import MongoClient
conn = MongoClient()
db = conn.zipp
collection = db.stateaddresses

countries = first_sheet.col_values(0)
# del countries[0]

India_States = first_sheet.col_values(1)
# del India_States[0]


address = raw_input("Enter address... \n")
tokend_address = address.split(",")
# for i in range(len(tokend_address)):
#     str(tokend_address[i]).capitalize()

print tokend_address

main_address = {}


if tokend_address[-1] in countries:
    print "hello"
    main_address["Country"] = tokend_address[-1]
    if tokend_address[-2] in India_States:
        main_address["State"] = tokend_address[-2]
        State = tokend_address[-2]
        dum_State = [i for i, x in enumerate(India_States) if x == State]
        print dum_State[0]
        print dum_State[-1]
        Districts = first_sheet.col_slice(start_rowx=dum_State[0]+1,end_rowx=dum_State[-1]+1,colx=2)
        xy = str(Districts[0])
        print xy[5:]
        print Districts
        if tokend_address[-3] in Districts:
            print "hey"
            main_address["District"] = tokend_address[-3]
            District = tokend_address[-3]
            dum_District = [i for i, x in enumerate(India_States) if x == District]
            Sub_Districts = first_sheet.col_slice(start_rowx=dum_District[0],end_rowx=dum_District[-1],colx=3)
            if tokend_address[-4] in Sub_Districts:
                main_address["Sub_District"] = tokend_address[-4]

print main_address