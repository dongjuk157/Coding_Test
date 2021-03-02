from sys import stdin
from collections import deque
input = stdin.readline

m, n = map(int, input().split())
q = deque()
tomato = []
for r in range(n):
    tmp = list(map(int, input().split()))
    tomato.append(tmp)
    for c in range(m):
        if tmp[c] == 1:
            q.append((r, c))
count = 0
tmp_q = deque()
#delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]

while q:
    r, c = q.popleft()
    for i in range(4):
        dr = r + dy[i]
        dc = c + dx[i]
        if 0 <= dr < n and 0 <= dc < m:
            if tomato[dr][dc] == 0:
                tomato[dr][dc] = 1
                tmp_q.append((dr,dc))
    if not q:
        q = tmp_q
        count += 1
        tmp_q = deque()
else:
    count -= 1
result = 0
break_chk = False
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            break_chk = True
            break
    if break_chk:
        break
if break_chk:
    result = -1
else:
    result = count
print(result)