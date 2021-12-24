# import sys; input = sys.stdin.readline
from heapq import heappop, heappush
INF = 200_000 * 1_000 * 2

def dijkstra(start, end, num_of_nodes):
    q = [(0, start)]
    visit = [INF for _ in range(num_of_nodes + 1)]
    visit[start] = 0
    while q:
        dist, cur = heappop(q)
        if visit[cur] < dist:
            continue
        for adj, adj_dist in linked_list[cur]:
            if visit[adj] > dist + adj_dist:
                visit[adj] = dist + adj_dist
                heappush(q, (visit[adj], adj))
    return visit[end]


# 0 입력
N, E = map(int, input().split())
linked_list = [list() for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    linked_list[a].append((b, c))
    linked_list[b].append((a, c))
v1, v2 = map(int, input().split())

# 1 최단경로 탐색
ans1 = dijkstra(1, v1, N) + dijkstra(v1, v2, N) + dijkstra(v2, N, N)
ans2 = dijkstra(1, v2, N) + dijkstra(v2, v1, N) + dijkstra(v1, N, N)
answer = min(ans1, ans2)
if answer >= INF:
    answer = -1
print(answer)


