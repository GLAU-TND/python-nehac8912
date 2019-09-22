r,c=list(map(int,input().split()))
m=[]
l=list(map(int,input().split()))
k=0
for i in range(r):
    a=[]
    for j in range(c):
        a.append(l[k])
        k+=1
    m.append(a)
for i in m:
    print(*i)