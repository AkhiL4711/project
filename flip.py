seq = list(raw_input())
# print seq
max_count = 0
now_zero = 0
now_one = 0
arr = []
l=[[0,1]]
r=[]
count = 0
def maxSubArraySum(a, size):
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i][0]
        if max_ending_here < 0:
            max_ending_here = 0
            ans = i
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return [max_so_far,ans+1]

for i in range(0,len(seq)):
    if seq[i] == "0":
        if now_zero == 0 and i != 0:
            arr.append((-now_one,count+1))
            now_one = 0
            count += 1
            l.append([i,count+1])
            r.append([i-1,count])
        now_zero += 1
    elif seq[i] == "1":
        if now_one == 0 and i != 0:
            arr.append((now_zero,count+1))
            now_zero = 0
            count += 1
            l.append([i,count+1])
            r.append([i-1,count])
        now_one += 1
if now_one != 0:
    arr.append((-now_one,count+1))
else:
    arr.append((now_zero,count+1))
r.append([len(seq),count+1])
# print arr
# print l
# print r
answer = maxSubArraySum(arr,len(arr))
# print answer
Result = [l[answer[1]][0],l[answer[1]][0]+answer[0]-1]
print Result
