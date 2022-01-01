# import sys;input = sys.stdin.readline
N, K = map(int, input().split())
v = [int(input()) for _ in range(N)]
a = 0
while 0 != K:
    share = K // v[-1]
    a += K // v[-1]
    K %= v[-1]
    v.pop()

print(a)