from heapq import heappop, heappush
N = int(input())
h = []
for i in range(N):
    x = int(input())
    if x > 0:
        heappush(h, x)
    elif x == 0:
        if h:
            print(heappop(h))
        else:
            print(0)