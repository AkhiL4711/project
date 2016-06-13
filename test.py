time = raw_input().strip("")
time_arr=time.split(":")

s=time_arr[2]
new = ''.join([i for i in s if not i.isdigit()])
result = ''.join([i for i in s if i.isdigit()])
del time_arr[2]
time_arr.append(result)
if (new== 'AM'):
    t=time_arr[0]
elif(new=='PM'):
    t=int(time_arr[0])+12
del time_arr[0]
time_arr.insert(-1,t)
x=":".join(set(time_arr))
print x