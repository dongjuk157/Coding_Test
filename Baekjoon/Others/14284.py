# import sys; input = sys.stdin.readline
from heapq import heappop, heappush
INF = 1234567890
def dijkstra(s, e, size, linked_list):
    h = [(0, s)]
    dist = [INF for _ in range(size + 1)]
    while h:
        cur_dist, cur = heappop(h)
        if cur == e:
            return cur_dist
        dist[cur] = cur_dist
        for adj_dist, adj in linked_list[cur]:
            if dist[adj] > cur_dist + adj_dist:
                heappush(h, (cur_dist + adj_dist, adj))
    return INF


def main():
    N, M = map(int, input().split())
    linked_list = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        linked_list[a].append((c, b))
        linked_list[b].append((c, a))
    s, t = map(int, input().split())

    return dijkstra(s, t, N, linked_list)

if __name__ == "__main__":
    print(main())
