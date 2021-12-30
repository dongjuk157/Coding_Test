T = int(input())
for tc in range(T):
    N = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    memo = [[0 for _ in range(N)] for _ in range(2)]
    for i in range(N):
        memo[0][i] = sticker[0][i]
        memo[1][i] = sticker[1][i]
        if i == 0:
            continue
        elif i == 1:
            memo[0][i] += memo[1][i - 1]
            memo[1][i] += memo[0][i - 1]
        else:
            memo[0][i] += max(memo[1][i - 1], memo[1][i - 2])
            memo[1][i] += max(memo[0][i - 1], memo[0][i - 2])

    print(sticker, memo)

    print(max(memo[0][-1], memo[1][-1]))