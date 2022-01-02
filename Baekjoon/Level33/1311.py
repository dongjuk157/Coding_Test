import sys;input = sys.stdin.readline
INF = 987654321
def backtrack(ind, limit, state, memo, d):
    if ind == limit:
        return 0
    if memo[ind][state] != -1: return memo[ind][state]
    memo[ind][state] = INF
    for i in range(limit):
        if state & (1 << i): continue
        next = state | (1 << i)
        memo[ind][state] = min(memo[ind][state], backtrack(ind + 1, limit, next, memo, d) + d[ind][i])
    return memo[ind][state]

def main():
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(N)]
    memo = [[-1 for _ in range(1 << N)] for _ in range(N)]
    answer = backtrack(0, N, 0, memo, d)
    print(answer)

if __name__ == '__main__':
    main()