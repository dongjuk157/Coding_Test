import sys;input = sys.stdin.readline
from heapq import heappop, heappush
h = []
for i in range(int(input())):
    x = int(input())
    if x:
        heappush(h, -x)
    else:
        print(-heappop(h) if h else 0)