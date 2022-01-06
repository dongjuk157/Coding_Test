import sys; input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    money = list(map(int, input().split()))
    M = int(input())
    memo = [1] + [0 for _ in range(M)]

    for m in money:
        for i in range(M + 1 - m):
            memo[i + m] += memo[i]

    print(memo[M])
