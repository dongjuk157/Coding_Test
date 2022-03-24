# import sys; input = sys.stdin.readline
from collections import deque
from itertools import combinations
d = [(0, -1), (-1, 0), (0, 1)]  # west/north/east


def bfs(turn, archers):
    global N, M, D, _map, dead
    ret = set()
    for archer in archers:  # [0, 1, 2] => start col
        q = deque()  # add archer's range
        a_pos = (len(_map) - turn, archer)
        q.append((a_pos[0] - 1, archer))
        visit = set()
        while q:
            cur = q.popleft()
            if cur in visit:
                continue
            visit.add(cur)
            if _map[cur[0]][cur[1]] and not dead[cur[0]][cur[1]]:
                ret.add(cur)
                break
            for dr, dc in d:
                nr, nc = cur[0] + dr, cur[1] + dc
                if 0 > nc or nc >= M: continue
                if abs(a_pos[0] - nr) + abs(a_pos[1] - nc) > D: continue
                q.append((nr, nc))
    for r in ret:
        dead[r[0]][r[1]] = 1
    return len(ret)


def main():
    global N, M, D, _map, dead
    N, M, D = map(int, input().split())
    _map = []
    # _map = [[0 for _ in range(M)] for _ in range(D - 1)]
    for _ in range(N):
        _map.append(list(map(int, input().split())))
    answer = 0
    for archers in combinations(range(M), 3):
        ans = 0
        dead = [[0 for _ in range(M)] for _ in range(len(_map))]
        for turn in range(N):
            ans += bfs(turn, archers)
        answer = max(answer, ans)
    print(answer)


if __name__ == "__main__":
    main()