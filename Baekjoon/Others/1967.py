import sys; input = sys.stdin.readline
from collections import deque
def bfs(start):
    q = deque([start])
    visit = [-1] * (n + 1)
    visit[start[0]] = 0
    ret = (0, 0)
    while q:
        cur, dist = q.popleft()
        for adj, adj_w in link_list[cur]:
            if visit[adj] != -1: continue
            visit[adj] = visit[cur] + adj_w
            q.append((adj, visit[adj]))
            if ret[1] < visit[adj]:
                ret = (adj, visit[adj])

    return ret

n = int(input())
link_list = [list() for _ in range(n + 1)]
for i in range(n - 1):
    n1, n2, w = map(int, input().split())
    link_list[n1].append((n2, w))
    link_list[n2].append((n1, w))

ret = bfs((1, 0))
ans = bfs((ret[0],0))
print(ans[1])