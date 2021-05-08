import sys; input = sys.stdin.readline
from collections import deque
V = int(input())
G = [list() for _ in range(V + 1)]
for _ in range(V):
    node = 0
    tmp_list = list(map(int, input().split()))
    for i in range(1, len(tmp_list) - 1, 2):
        G[tmp_list[0]].append((tmp_list[i], tmp_list[i + 1]))

ans = 0
def bfs(start):
    global ans
    visit = [-1] * (V + 1)
    visit[start[0]] = 0
    q = deque([start])
    ret = (0, 0)
    while q:
        cur, w = q.popleft()
        for adj, adj_w in G[cur]:
            if visit[adj] != -1: continue
            visit[adj] = visit[cur] + adj_w
            q.append((adj, adj_w))
            if ret[1] < visit[adj]:
                ret = (adj, visit[adj])
    return ret
ret = bfs((1, 0))
ans = bfs((ret[0], 0))
print(ans[1])
