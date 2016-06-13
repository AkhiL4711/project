t=raw_input()
result=[]
for x in range(int(t)):
    y=raw_input().split()
    n=y[0]
    k=y[1]
    e=y[2]
    m=y[3]
    marks=[]
    for i in range(int(n)-1):
        marks.append(raw_input().split())
    total=[]
    for j in range(int(n)-1):
        tot=0
        for l in range(int(e)):
            tot+=int(marks[j][l])
        total.append(tot)
    to=sorted(total)
    my=raw_input().split()
    t=0
    for i in range(len(my)):
        t+=int(my[i])
    result.append(str(int(to[int(n)-int(k)-1])-int(t)+1))
ans=" ".join(result)
print ans
