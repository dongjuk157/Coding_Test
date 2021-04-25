N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * i for i in range(1, len(triangle) + 1)]
dp[0][0] = triangle[0][0]
for i in range(1, len(dp)):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = triangle[i][j] + dp[i - 1][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i - 1][j],dp[i - 1][j - 1])
print(max(dp[-1]))