from collections import deque
def main():
    n, k = map(int, input().split())
    memo = [200000 for _ in range(100001)]
    q = deque()
    q.append(n)
    memo[n] = 0
    answer = None
    while q:
        cur = q.popleft()
        if cur == k:
            answer = memo[cur]
            break
        if 2 * cur <= 100000:
            if memo[2 * cur] > memo[cur]:
                memo[2 * cur] = memo[cur]
                q.append(2 * cur)

        if cur - 1 >= 0:
            if memo[cur - 1] > memo[cur]:
                memo[cur - 1] = memo[cur] + 1
                q.append(cur - 1)

        if cur + 1 <= 100000:
            if memo[cur + 1] > memo[cur]:
                memo[cur + 1] = memo[cur] + 1
                q.append(cur + 1)
    print(answer)

if __name__ == "__main__":
    main()
