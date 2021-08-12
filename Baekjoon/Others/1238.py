from sys import stdin;input = stdin.readline
from heapq import heappop, heappush
def dijkstra(start, linked_list, distance):
    heap = [(0, start)]
    distance[start] = 0
    while heap:
        cur_w, cur = heappop(heap)
        if distance[cur] < cur_w: continue
        for adj, adj_w in linked_list[cur]:
            if distance[adj] > adj_w + cur_w:
                distance[adj] = adj_w + cur_w
                heappush(heap, (distance[adj], adj))

N, M, X = map(int, input().split())
linked_list1 = [list() for _ in range(N + 1)]
linked_list2 = [list() for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    linked_list1[s].append((e, w))
    linked_list2[e].append((s, w))

INF = 2100000000
dist1 = [INF for _ in range(N + 1)]
dist2 = [INF for _ in range(N + 1)]
dijkstra(X, linked_list1, dist1)
dijkstra(X, linked_list2, dist2)

answer = 0
for i in range(1, N + 1):
    tmp = dist1[i] + dist2[i]
    if answer < tmp:
        answer = tmp
print(answer)

