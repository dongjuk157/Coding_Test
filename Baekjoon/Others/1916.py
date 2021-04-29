import sys
input = sys.stdin.readline
from heapq import heappop, heappush
N = int(input())
M = int(input())
link_arr = [list() for _ in range(N + 1)]
for _ in range(M):
    st, en, we = map(int, input().split())
    link_arr[st].append((en, we))

# dijkstra
start, end = map(int, input().split())
inf = 10 ** 10
visit = [0] * (N + 1)
dist = [inf] * (N + 1)
q = [(0, start)]
dist[start] = 0
while q:
    w, cur = heappop(q)
    visit[cur] = 1
    for adj_node, adj_w in link_arr[cur]:
        if not visit[adj_node] and dist[adj_node] > dist[cur] + adj_w:
            dist[adj_node] = dist[cur] + adj_w
            heappush(q, (dist[adj_node], adj_node))
print(dist[end])