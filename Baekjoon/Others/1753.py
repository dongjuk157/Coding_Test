import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N, E = map(int, input().split())
K = int(input())
link = [list() for _ in range(N + 1)]
for _ in range(E):
    n1, n2, w = map(int, input().split())
    link[n1].append((w, n2))

# 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리
visit = set()
dist = [3000000] * (N + 1)
dist[K] = 0
q = [(0, K)]
while q:
    # 가중치가 가장 작은 노드 탐색
    w, node = heappop(q)
    if node in visit: continue
    visit.add(node)
    for idx in range(len(link[node])):
        adj_w, adj_node = link[node][idx]
        if adj_node in visit: continue
        # 방문하지 않은 점의 가중치보다 (현재 점 +가중치)의 값이 작으면 갱신
        if dist[adj_node] > dist[node] + adj_w:
            dist[adj_node] = dist[node] + adj_w
            # 가중치 순서 최소힙 추가
            heappush(q, (dist[adj_node], adj_node))

for i in range(1, N + 1):
    if dist[i] == 3000000:
        print("INF")
    else:
        print(dist[i])
