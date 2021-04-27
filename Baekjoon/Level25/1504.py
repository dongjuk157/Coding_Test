import sys
input = sys.stdin.readline
from heapq import heappop, heappush
N, E = map(int, input().split())
link_arr = [list() for _ in range(N + 1)]
for _ in range(E):
    n1, n2, w = map(int, input().split())
    link_arr[n1].append((n2, w))
    link_arr[n2].append((n1, w))
v1, v2 = map(int, input().split())

# inf = 800*1000 설정
# 모든 정점을 지나가도 지나가는 최소 정점의 개수는 (N-1)개 이기때문
result_list = []
def dijkstra(start, end1):
    if start==end1:
        return 0
    dist = [800000] * (N + 1)
    visit = [0] * (N + 1)
    q = [(0, start)] # weight, start
    dist[start] = 0
    while q:
        w, cur = heappop(q)
        visit[cur] = 1
        if cur == end1:
            return dist[cur]
        for i in range(len(link_arr[cur])):
            adj, adj_w = link_arr[cur][i]
            if not visit[adj] and dist[adj] > dist[cur] + adj_w:
                dist[adj] = dist[cur] + adj_w
                heappush(q, (dist[adj], adj))
    return 8000000
# 1. 1-> v1 -> v2 -> N
result1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
# 2. 1-> v2 -> v1 -> N
result2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)
result = min(result1, result2)
if result >= 800000:
    result = -1

print(result)
