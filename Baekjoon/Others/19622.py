# import sys; input = sys.stdin.readline
def main():
    N = int(input())
    memo = [0 for _ in range(N)]
    for i in range(N):
        s, e, m = map(int, input().split())
        if i == 0:
            memo[i] = m
        elif i == 1:
            memo[i] = max(memo[i - 1], m)
        else:
            memo[i] = max(memo[i - 1], memo[i - 2] + m)
    print(memo[-1])


if __name__ == "__main__":
    main()
