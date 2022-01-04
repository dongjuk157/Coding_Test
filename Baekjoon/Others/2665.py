# import sys; input = sys.stdin.readline
from heapq import heappop, heappush

def dijkstra(N):
    visit = [[False for _ in range(N)] for _ in range(N)]
    h = [(0, 0, 0)]  # cost, r, c

    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while h:
        cost, r, c = heappop(h)
        if r == N - 1 and c == N - 1:
            return cost
        if visit[r][c]:
            continue
        visit[r][c] = True
        for i in range(4):
            dr, dc = r + d[i][0], c + d[i][1]
            if dr < 0 or dr >= N or dc < 0 or dc >= N:
                continue

            if _map[dr][dc] == '1':
                heappush(h, (cost, dr, dc))
            else:
                heappush(h, (cost + 1, dr, dc))

    # 혹시라도 에러가 발생하는 경우, -1 반환. 못찾는 경우는 없음
    return -1

N = int(input())
_map = [input().rstrip() for _ in range(N)]
print(dijkstra(N))




