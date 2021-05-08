# 분할정복
import sys; input = sys.stdin.readline
a, b, c = map(int, input().split())
def divNconq(a, b, c):
    if b == 1:
        return a % c
    tmp_a = divNconq(a, b // 2, c)
    return a * tmp_a * tmp_a % c if b & 1 else tmp_a * tmp_a % c
print(divNconq(a,b,c))
