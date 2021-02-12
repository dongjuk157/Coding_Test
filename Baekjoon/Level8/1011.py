import sys
from math import sqrt
input = sys.stdin.readline
t=int(input())

for tc in range(t):
    x,y=map(int,input().split())
    distance = y-x
    n=int(sqrt(distance))

    if (n**2) == distance:
        print(2*n - 1)
    elif distance <= (n**2 +n):
        print(2*n)
    else: # distance <= (n**2 + 2*n):
        print(2*n + 1)
