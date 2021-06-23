from heapq import heappop, heappush

def solution(N, road, K):
    INF = 5000000
    answer = 0
    g = [[] for _ in range(N + 1)]
    for i in range(len(road)):
        g[road[i][0]].append((road[i][1], road[i][2]))
        g[road[i][1]].append((road[i][0], road[i][2]))

    dist = [INF] * (N + 1)
    visit = [0] * (N + 1)
    q = [(0, 1)]  # start = 1
    dist[1] = 0
    while q:
        weight ,cur = heappop(q)
        if visit[cur]: continue
        visit[cur] = 1
        for i in range(len(g[cur])):
            if weight + g[cur][i][1] < dist[g[cur][i][0]]:
                dist[g[cur][i][0]] = weight + g[cur][i][1]
                heappush(q, (dist[g[cur][i][0]], g[cur][i][0]))

    return len([i for i in dist if i <= K])


from collections import deque
def solution2(N, road, K):
    INF = 5000000
    g = [[] for _ in range(N + 1)]
    dist = [INF] * (N + 1)
    for i in range(len(road)):
        g[road[i][0]].append((road[i][1], road[i][2]))
        g[road[i][1]].append((road[i][0], road[i][2]))

    q = deque()  # start = 1
    q.append((1, 0))
    dist[1] = 0
    while q:
        cur, weight = q.popleft()
        for i in range(len(g[cur])):
            if weight + g[cur][i][1] < dist[g[cur][i][0]]:
                dist[g[cur][i][0]] = weight + g[cur][i][1]
                q.append((g[cur][i][0], dist[g[cur][i][0]]))

    return len([i for i in dist if i <= K])

if __name__ == '__main__':
    N = 5
    road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
    K = 3
    result = 4
    print(solution(N, road, K) == result)

    N = 6
    road = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
    K = 4
    result = 4
    print(solution2(N, road, K) == result)