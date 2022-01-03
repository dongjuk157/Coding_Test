import sys; input = sys.stdin.readline
INF = 1234567890
def backtrack(cur, limit, state, memo, arr):
    if state == (1 << limit) - 1:
        if arr[cur][0]:
            return arr[cur][0]
        return INF

    if memo[cur][state] != -1: # check visit
        return memo[cur][state]

    memo[cur][state] = INF
    for i in range(limit):
        if cur == i:            continue
        if state & (1 << i):    continue
        if not arr[cur][i]:     continue

        next_state = state | (1 << i)
        next_val = backtrack(i, limit, next_state, memo, arr) + arr[cur][i]

        if memo[cur][state] > next_val:
            memo[cur][state] = next_val
    return memo[cur][state]

def main():
    N = int(input())
    _map = [list(map(int, input().split())) for _ in range(N)]
    memo = [[-1 for _ in range(1 << N)] for _ in range(N)]
    answer = backtrack(0, N, 1, memo, _map)

    print(answer)

if __name__ == '__main__':
    main()