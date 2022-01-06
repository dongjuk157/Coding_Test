import sys; input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    money = list(map(int, input().split()))
    M = int(input())
    memo = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            tmp = 0
            tmp += memo[i - 1][j]
            if j == money[i - 1]:
                tmp += 1
            elif j - money[i - 1] > 0:
                tmp += memo[i][j - money[i - 1]]
            memo[i][j] = tmp

    print(memo[N][M])