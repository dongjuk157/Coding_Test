from collections import deque
from sys import stdin
input = stdin.readline

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                q.append((i, j, k))

count = 0
def bfs(array, queue):
    global count
    tmp_q = deque()
    dz = [0, 0, 0, 0, -1, 1]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [-1, 1, 0, 0, 0, 0]
    while queue:
        dh, dr, dc = queue.popleft()
        for i in range(6):
            if dh + dz[i] < 0 or dh + dz[i] >= h: continue
            if dr + dy[i] < 0 or dr + dy[i] >= n: continue
            if dc + dx[i] < 0 or dc + dx[i] >= m: continue
            if array[dh + dz[i]][dr + dy[i]][dc + dx[i]] == 0:
                array[dh + dz[i]][dr + dy[i]][dc + dx[i]] = 1
                tmp_q.append((dh + dz[i], dr + dy[i], dc + dx[i]))
        if not queue:
            if not tmp_q: return
            queue = tmp_q
            count += 1
            tmp_q = deque()
bfs(tomato, q)

def break_chk(_list):
    for i in range(len(_list)):
        for j in range(len(_list[0])):
            for k in range(len(_list[0][0])):
                if tomato[i][j][k] == 0:
                    return True
    return False

if break_chk(tomato):
    print(-1)
else:
    print(count)