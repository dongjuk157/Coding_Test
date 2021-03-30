from collections import deque
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(q):
    while q:
        x, y = q.popleft()
        chk = -2 if visit[x][y] == -2 else visit[x][y]
        for i in range(4):
            dx = x + delta[i][0]
            dy = y + delta[i][1]
            if dx < 0 or dx >= h or dy < 0 or dy >= w:
                if chk != -2:
                    return visit[x][y] + 1
            else:
                if visit[dx][dy] == -1 and (building[dx][dy] == '.' or building[dx][dy] == '@'):
                    if chk == -2:
                        visit[dx][dy] = -2
                    else:
                        visit[dx][dy] = visit[x][y] + 1
                    q.append((dx, dy))

    return "IMPOSSIBLE"

for tc in range(int(input())):
    w, h = map(int, input().split())
    building = []
    start = []
    fire = []
    visit = [[-1] * w for _ in range(h)]
    for i in range(h):
        tmp = input()
        building.append(tmp)
        for j in range(w):
            if tmp[j] == '*':
                fire.append((i, j))
                visit[i][j] = -2
            elif tmp[j] == '@':
                start = (i, j)
                visit[i][j] = 0
    q = deque()
    q.extend(fire) #불을 먼저 넣어서 진행
    q.append(start)

    print(bfs(q))

