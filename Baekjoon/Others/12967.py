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
# 0 ≤ p < q < r < N 이면서, A[p] * A[q] * A[r]이 K로 나누어 떨어지는 (p, q, r) 쌍의 개수
# N의 원소와 K 의 최대공약수
n_gcd = [[0]* 2 for i in range(N)]
for i in range(N):
    n_gcd[i][0] = n_list[i]
print(n_gcd)
result = 0
def backtrack(index=0, total=1, start=-1, arr=[]):
    if index == 3:
        print(arr, total)
        if not total % K:
            global result
            result += 1
    else:
        for i in range(start + 1, N):
            backtrack(index+1, total*n_list[i], i, arr+[n_list[i]])
backtrack()

print(result)


