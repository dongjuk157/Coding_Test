import sys; input = sys.stdin.readline
from collections import deque

def bfs():
    is_change = False
    visit = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                visit[i][j] = 1
                ret = [(i,j)]
                q = deque([(i,j)])
                population = N_map[i][j]
                while q:
                    y, x = q.popleft()
                    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        yy = y + dy
                        xx = x + dx
                        # 주어진 나라의 크기를 넘는 경우, 방문한 경우
                        if 0 <= yy < N and 0 <= xx < N and not visit[yy][xx]:
                            # 인구 차이가 안나는 경우
                            if L <= abs(N_map[yy][xx] - N_map[y][x]) <= R:
                                visit[yy][xx] = 1
                                population += N_map[yy][xx]
                                q.append((yy, xx))
                                ret.append((yy, xx))
                if len(ret) > 1:
                    is_change = True
                    population = population // len(ret)
                    for x, y in ret:
                        N_map[x][y] = population
    return is_change


N, L, R = map(int, input().split())
N_map = [list(map(int, input().split())) for _ in range(N)]
answer = 0
while True:
    if bfs():
        answer += 1
    else:
        break

print(answer)