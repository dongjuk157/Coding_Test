from itertools import combinations
from math import isqrt
max_limit = 1000*9
prime = [True for _ in range(max_limit + 1)]
prime[0], prime[1] = False, False
for i in range(2, isqrt(max_limit) + 1):
    if prime[i]:
        for j in range(i + i, max_limit + 1, i):
            prime[j] = False

def main():
    N, M = map(int, input().split())
    ans = set()
    for i in combinations(map(int, input().split()), M):
        tmp = sum(i)
        if prime[tmp]:
            ans.add(tmp)
    if len(ans):
        print(*sorted(ans))
    else:
        print(-1)

if __name__ == '__main__':
    main()
