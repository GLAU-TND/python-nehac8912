n = int(input())
res = list(map(int,input().split(' ')))
c = 0
m = 0
for i in range(n):
    if c < res[i]:
        c = res[i]
for i in range(n):
    if c == res[i]:
        m += 1
print(m)