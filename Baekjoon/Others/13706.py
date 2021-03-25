# overflow Error
# from math import sqrt
# print(sqrt(int(input())))

# overflow Error
# N = int(input()) # 800 자리
# print((int(input())**0.5))

# 내가 푼 방식
from math import isqrt
print(isqrt(int(input())))

# 이분탐색
n = int(input())
low = 1
high = n

while 1:
    mid = (low + high) // 2
    if mid ** 2 == n:
        print(mid)
        break
    elif mid ** 2 > n:
        high = mid - 1
    elif mid ** 2 < n:
        low = mid + 1