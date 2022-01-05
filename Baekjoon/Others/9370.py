# import sys; input = sys.stdin.readline
from heapq import heappop, heappush
INF = 987654321


def check_visit_all(dest_list, visit):
    for item in dest_list:
        if not visit[item]:
            return False
    return True


def dijkstra(start, size, destination):
    visit = [False for _ in range(size + 1)]
    dist_list = [INF for _ in range(size + 1)]
    mh = [(0, start)]
    while mh:
        dist, cur = heappop(mh)
        if visit[cur]: continue
        visit[cur] = True
        dist_list[cur] = dist
        if check_visit_all(destination, visit):
            break
        for adj_dist, adj in map_linked_list[cur]:
            if dist + adj_dist < dist_list[adj]:
                heappush(mh, (dist + adj_dist, adj))

    return dist_list

T = int(input())
for _ in range(T):
    # 0 입력
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    map_linked_list = [list() for _ in range(n + 1)]
    dist_tmp = 0
    for i in range(m):
        a, b, d = map(int, input().split())
        if (a == g and b == h) or (a == h and b == g):
            dist_tmp = d
        map_linked_list[a].append((d, b))
        map_linked_list[b].append((d, a))
    destinations = set()
    for i in range(t):
        destinations.add(int(input()))

    # 1 탐색
    s_list = dijkstra(s, n, destinations)
    h_list = dijkstra(h, n, destinations)
    g_list = dijkstra(g, n, destinations)
    answer = set()
    for dest in destinations:
        tmp1 = s_list[g] + dist_tmp + h_list[dest]
        tmp2 = s_list[h] + dist_tmp + g_list[dest]
        if s_list[dest] == tmp1 or s_list[dest] == tmp2:
            answer.add(dest)

    # 2 출력
    print(*sorted(answer))