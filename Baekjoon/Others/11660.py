import sys; input = sys.stdin.readline
def main():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    memo = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            memo[i][j] = memo[i][j-1] + memo[i-1][j] - memo[i-1][j-1] + arr[i-1][j-1]
    print(*memo, sep='\n')
    answer = []
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        ans = memo[x2][y2] - memo[x1 - 1][y2] - memo[x2][y1 - 1] + memo[x1 - 1][y1 - 1]
        answer.append(ans)
    print('\n'.join(map(str, answer)))


if __name__ == "__main__":
    main()
