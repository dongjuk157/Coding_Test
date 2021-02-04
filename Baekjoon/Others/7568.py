import sys
input= sys.stdin.readline

n=int(input())

dungchi = list()
for i in range(n):
    dungchi.append(tuple(map(int,input().split())))
    
result=[]
for i in range(n):
    chk = 0
    for j in range(n):
        if dungchi[i][0]<dungchi[j][0] and dungchi[i][1]<dungchi[j][1] :
            chk += 1
    result.append(str(chk+1))

print(' '.join(result))
