N = int(input())
nums = list(map(int, input().split()))
dp = [-200000000 for _ in range(N + 1)]
for i in range(N):
    dp[i + 1] = max(dp[i] + nums[i], nums[i])

print(max(dp))



