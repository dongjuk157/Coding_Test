import sys
sys.stdin = open('2636_input.txt','r')
from collections import deque
def bfs(q):
    melting = 0
    melt_list = set()
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + delta[i][0]
            dy = y + delta[i][1]
            if dx < 0 or dx >= h + 2 or dy <0 or dy >= w + 2: continue
            if visited[dx][dy]: continue
            if matrix[dx][dy]==0:
                q.append((dx, dy))
                visited[dx][dy] = 1
            else:
                melt_list.add((dx, dy))

    return melt_list

h, w = map(int, input().split())
matrix = []
for i in range(h + 2):
    if i ==0 or i == h+1:
        matrix.append([0] * (w + 2))
    else:
        tmp = list(map(int, input().split()))
        matrix.append([0] + tmp + [0])
visited = [[0] * (w + 2) for _ in range(h + 2)]
q = deque()
# print(*matrix, sep='\n', end='\n\n')
# print(*visited, sep='\n', end='\n\n')
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result_time, result_cheese = -1, 0
old = 0

q.append((0, 0))
visited[0][0] = 1
while q:
    melt = bfs(q)
    result_time += 1
    result_cheese = old
    q.extend(melt)
    old = len(melt)
    while melt:
        x,y = melt.pop()
        matrix[x][y] = 0
#    print(result_time, result_cheese, old)


print(result_time, result_cheese)