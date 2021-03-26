# pqr
# 계속 시간 초과해서 못풀었다.
import sys
input = sys.stdin.readline
from itertools import combinations
def gcd(y, x):
    if y < x: # 항상 y가 더 크게
        y, x = x, y
    while x != 0:
        t = y % x
        y, x = x, t
    return abs(y)

N, K = map(int, input().split())
n_list = list(map(int, input().split()))
# N의 원소와 K 의 최대공약수
n_gcd = [0] * N
for i in range(N):
    n_gcd[i] = gcd(n_list[i], K)

result = 0
for x, y, z in combinations(n_gcd, 3):
    if gcd(x*y*z, K) == K:
        result += 1
print(result)


