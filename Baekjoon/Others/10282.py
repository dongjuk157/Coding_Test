import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start, size, adj_list):
    ret = [0, 0]
    h = [(0, start)]
    visit = [0 for _ in range(size + 1)]
    while h:
        dist, cur = heappop(h)
        if visit[cur]: continue
        visit[cur] = 1
        ret[1] = max(ret[1], dist)
        for adj_dist, adj in adj_list[cur]:
            heappush(h, (adj_dist + dist, adj))
    ret[0] = sum(visit)
    return ret

def main():
    answer = []
    for _ in range(int(input())):
        # 1 input
        n, d, c = map(int, input().split())
        adj_list = [[] for _ in range(n + 1)]
        for _ in range(d):
            a, b, s = map(int, input().split())
            adj_list[b].append((s, a))
        # 2 dijkstra and output
        answer.append(dijkstra(c, n, adj_list))

    for a in answer:
        print(*a)


if __name__ == "__main__":
    main()
