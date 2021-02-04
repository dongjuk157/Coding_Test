import sys
input=sys.stdin.readline
n = int(input())

lst= list(map(int,input().split()))
lst.sort()
result = 0
for i in range(n):
    result+= lst.pop()*(i+1)
print(result)
