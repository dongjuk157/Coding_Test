# import sys; input = sys.stdin.readline
from collections import deque


def bfs():
    global N, M, _map, viruses
    ret = 0
    visit = [[0 for _ in range(M)] for _ in range(N)]
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 1 breadth first search
    q = deque()
    for virus in viruses:
        q.append(virus)

    while q:
        vr, vc = q.popleft()
        if visit[vr][vc]:
            continue
        visit[vr][vc] = 1
        for dd in d:
            nvr = vr + dd[0]
            nvc = vc + dd[1]
            if 0 > nvr or nvr >= N or 0 > nvc or nvc >= M:
                continue
            if visit[nvr][nvc]:
                continue
            if _map[nvr][nvc] == 1:
                continue
            q.append((nvr, nvc))


    # 3 After BFS, calculate safe area
    for r in range(N):
        for c in range(M):
            if not visit[r][c] and not _map[r][c]:
                ret += 1

    return ret


def backtrack(ind, count):
    global N, M, _map, answer
    if count == 3:
        # 2 BFS for spreading virus
        tmp = bfs()
        answer = max(answer, tmp)
        return
    if ind == N * M:
        return
    # 1  backtracking for selecting wall position
    # ind = r * M + c
    r = ind // M
    c = ind % M
    if not _map[r][c]:
        _map[r][c] = 1
        backtrack(ind+1, count+1)
        _map[r][c] = 0
    backtrack(ind+1, count)


def main():
    # 0 input
    global N, M, _map, viruses, answer
    N, M = map(int, input().split())
    _map = []
    viruses = []
    for i in range(N):
        _map.append(list(map(int, input().split())))
        for j in range(M):
            if _map[i][j] == 2:
                viruses.append((i, j))

    # 1 calculate max area
    answer = 0
    backtrack(0, 0)

    # 2 output
    print(answer)

if __name__ == "__main__":
    main()

