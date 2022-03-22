import sys; input = sys.stdin.readline
from collections import deque
from itertools import combinations

INF = 1234567890
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs(start_indexes):
    global N, M, _map, viruses
    visit = [[0 for _ in range(N)] for _ in range(N)]
    q = deque()
    for idx in start_indexes:
        q.append([0, *viruses[idx]])
    while q:
        dist, r, c = q.popleft()
        if visit[r][c]:
            continue
        visit[r][c] = dist
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N \
                    and not visit[nr][nc]:
                if _map[nr][nc] != 1:  # empty space
                    q.append([dist + 1, nr, nc])


    # check empty space and find max value
    ret = 0
    for i in range(N):
        for j in range(N):
            if _map[i][j]: continue
            if not visit[i][j]:
                return INF
            ret = max(ret, visit[i][j])
    return ret


def main():
    global N, M, _map, viruses
    # 0 input
    N, M = map(int, input().split())
    _map = []
    viruses = []
    for i in range(N):
        _map.append(list(map(int, input().split())))
        for j in range(N):
            if _map[i][j] == 2:
                viruses.append([i, j])

    # 1 bfs for combination with M viruses
    answer = INF
    for indexes in combinations(range(len(viruses)), M):
        answer = min(answer, bfs(indexes))

    # 2 output, print answer
    if answer == INF:
        print(-1)
    else:
        print(answer)


if __name__ == "__main__":
    main()
