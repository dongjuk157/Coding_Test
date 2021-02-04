n,m=map(int,input().split())
r,c =list(),list()

castle=[]
for _ in range(n):
    tmp=input()
    r.append(tmp.count('X'))
    castle.append(tmp)


for j in range(m):
    cnt = 0
    for i in range(n):
        if castle[i][j] == 'X':
            cnt += 1
    c.append(cnt)

print(max(r.count(0),c.count(0)))