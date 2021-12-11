from collections import deque
direct = [-1, 0, 1, 0, 0, -1, 0, 1]
_map = [
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0],
]
visit = [[0 for _ in range(len(_map[0]))] for _ in range(len(_map))]
start = (0, 0)
end = (0, 4)
def bfs(start, end):
    q = deque()
    q.append(start)
    while q:
        r, c = q.popleft()
        if (r, c) == end:
            break
        for i in range(4):
            dr = direct[2 * i]
            dc = direct[2 * i + 1]
            rr = r + dr
            cc = c + dc
            if not (0 <= rr < 4 and 0 <= cc < 5): continue
            if _map[rr][cc]: continue
            if visit[rr][cc]: continue
            visit[rr][cc] = visit[r][c] + 1
            q.append((rr, cc))
    return visit[end[0]][end[1]]
print(bfs(start, end))





