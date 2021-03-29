from collections import deque
n, k = map(int, input().split())
dp = [0] * 100001
q = deque([n])
dp[n] = 1
while q:
    x = q.popleft()
    if 0 <= x - 1 and dp[x - 1] == 0:
        dp[x - 1] = dp[x] + 1
        q.append(x - 1)
    if x + 1 <= 100000 and dp[x + 1] == 0:
        dp[x + 1] = dp[x] + 1
        q.append(x + 1)
    if x <= 50000 and dp[2 * x] == 0:
        dp[2 * x] = dp[x] + 1
        q.append(2 * x)
    if dp[k]:
        break
print(dp[k]-1)

