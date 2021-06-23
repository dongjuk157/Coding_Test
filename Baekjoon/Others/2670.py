import sys; input = sys.stdin.readline
n = int(input())
nums = [float(input()) for _ in range(n)] # 10 곱하면 출력할땐 0.001 곱할것
dp = [1] * (n + 1)
for i in range(1, n+1):
    if nums[i - 1]:
        dp[i] = dp[i - 1] * nums[i - 1]
    else:
        dp[i] = 0
max_ind = dp.index(max(dp))
min_ind = 0
for i in range(max_ind):
    pass
print(dp)
# print(max(dp), min(dp[:max_ind]))
print("{:0.3f}".format(dp[max_ind]/dp[min_ind]))

# 이렇게 하면 0이 들어오는 경우를 못찾음



