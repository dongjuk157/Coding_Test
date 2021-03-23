dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for tc in range(int(input())):
    N = int(input())
    for i in range(len(dp), N + 1):
        dp.append(dp[i - 1] + dp[i - 5])
    print(dp[N])