# import sys; input = sys.stdin.readline
from collections import deque
def bfs(i, j, _map, visit):
    global n, m
    ret = [0, 0]
    q = deque()
    q.append((i, j))
    while q:
        r, c = q.popleft()
        if visit[r][c]: continue
        visit[r][c] = 1
        if _map[r][c] == 'o':
            ret[0] += 1
        elif _map[r][c] == 'v':
            ret[1] += 1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 > nr or nr >= n or 0 > nc or nc >= m: continue
            if _map[nr][nc] == '#': continue
            q.append((nr, nc))

    if ret[0] > ret[1]:
        ret[1] = 0
    else:
        ret[0] = 0

    return ret

def main():
    global n, m
    n, m = map(int, input().split())
    _map = [list(input().rstrip()) for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    answer = [0, 0]
    for i in range(n):
        for j in range(m):
            if _map[i][j] == '#': continue
            if visit[i][j]: continue
            ret_val = bfs(i, j, _map, visit)
            answer[0] += ret_val[0]
            answer[1] += ret_val[1]
    print(*answer)

if __name__ == "__main__":
    main()
