n = int(input())
stair = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(stair[-1])
else:
    dp = [0] * (n + 1)
    dp[0] = stair[0]
    dp[1] = max(stair[0] + stair[1], stair[1])
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])
    print(dp[-1])

