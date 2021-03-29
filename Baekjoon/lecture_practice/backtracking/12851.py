from collections import deque
n, k = map(int, input().split())
if n == k:
    print(0)
    print(1)
else:
    dp = [0] * 100001
    q = deque([n])
    dp[n] = 1
    size, depth, cnt = len(q), 0, 0
    if_chk = True
    limit = 100000
    result_val = 0
    while q:
        if cnt == size:
            cnt = 0
            size =len(q)
            depth += 1
        cnt += 1
        x = q.popleft()
        if 0 <= x - 1 and (dp[x - 1] == 0 or dp[x - 1] == dp[x] + 1):
            dp[x - 1] = dp[x] + 1
            q.append(x - 1)
            if x - 1 == k:
                result_val += 1
        if x + 1 <= 100000 and (dp[x + 1] == 0 or dp[x + 1] == dp[x] + 1):
            dp[x + 1] = dp[x] + 1
            q.append(x + 1)
            if x + 1 == k:
                result_val += 1
        if x <= 50000 and (dp[2 * x] == 0 or dp[x * 2] == dp[x] + 1):
            dp[2 * x] = dp[x] + 1
            q.append(2 * x)
            if x * 2 == k:
                result_val += 1
        if if_chk and dp[k]:
            if_chk = False
            limit = dp[k] - 1
        if depth >= limit:
            break
    # result = limit
    print(limit)
    print(result_val)