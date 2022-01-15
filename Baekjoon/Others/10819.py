visit = None
numbers = None
ans = None
def backtrack(ind, limit, total, prev):
    global visit, numbers, ans
    if ind == limit:
        ans = max(ans, total)
        return

    for i in range(limit):
        if visit[i]: continue
        visit[i] = True
        # 1 2 3 => 1- 2 + 2- 3 => 총 두번
        if ind == 0:
            backtrack(ind + 1, limit, total, prev=i)
        else:
            backtrack(ind + 1, limit, total + abs(numbers[i] - numbers[prev]), prev=i)
        visit[i] = False


def main():
    global visit, numbers, ans
    N = int(input())
    numbers = list(map(int, input().split()))
    visit = [False for _ in range(N)]
    ans = 0
    backtrack(0, N, 0, 0)
    print(ans)
if __name__ == "__main__":
    main()