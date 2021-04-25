#점화식 어떻게 세워야하지?
# 10 50 9 20 30 50
# 1 2 1 2 3 4
# 10 50 9 20 30 60
# 1 2 1 2 3 4

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    max_val = 0
    for j in range(i):
        if arr[j] < arr[i] and max_val < dp[j]:
            max_val = dp[j]
    dp[i] = max_val + 1
print(dp)
print(max(dp))