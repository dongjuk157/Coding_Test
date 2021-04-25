n = int(input())
wine = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 1)
# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
# 최대 두잔 연속
dp[1] = wine[1]
if n >= 2:
    dp[2] = max(wine[1]+wine[2], dp[0] + wine[2])
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])
        dp[i] = max(dp[i - 1], dp[i])
print(dp[-1])
