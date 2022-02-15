# import sys; input = sys.stdin.readline
from heapq import heappop, heappush

def dijkstra(s, e, adj_list):
    INF = 987654321
    ret = None # dist, route
    h = [(0, [s], s)]
    visit = [0 for _ in range(len(adj_list))]
    while h:
        dist, route, cur = heappop(h)
        if cur == e:
            ret = (str(dist), str(len(route)), ' '.join(map(str, route)))
            break
        if visit[cur]:
            continue
        visit[cur] = 1
        for adj_dist, adj in adj_list[cur]:
            heappush(h, (adj_dist + dist, route+[adj], adj))

    return ret

def main():
    n, m = int(input()), int(input())
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, c = map(int, input().split())
        adj_list[s].append((c, e))
    s, e = map(int, input().split())
    answer = dijkstra(s, e, adj_list)
    print('\n'.join(answer))

if __name__ == "__main__":
    main()
