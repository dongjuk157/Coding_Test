# import sys; input = sys.stdin.readline
arr = [[False]*10000 for _ in range(10000)]
N = int(input())
for _ in range(N):
    x, y, w, h = map(lambda x: int(10 * float(x)),input().split())
    for i in range(w):
        for j in range(h):
            arr[x+i][y+j] = True

total = 0
for i in range(10000):
    total += sum(arr[i])
print("{:.2f}".format(total/100))


