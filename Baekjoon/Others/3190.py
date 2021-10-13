# import sys; input = sys.stdin.readline
from collections import deque
N = int(input())
K = int(input())
apples = set([tuple(map(int, input().split())) for _ in range(K)])
L = int(input())
change = [input().split() for _ in range(L)]
change_i = 0

_map = []
for i in range(N + 2):
    if i == 0 or i == N + 1:
        _map.append([-1 for _ in range(N + 2)])
    else:
        _map.append([-1] + [0 for _ in range(N)] + [-1])
# print(*_map, sep='\n')
# print(apples, change)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dir_i = 0 # 0,1,2,3 => r,d,l,u
pos_q = deque()
pos_q.append((1, 1))
time = 0
while True:
    time += 1
    # print(dir_i, time)
    r = pos_q[-1][0] + dr[dir_i]
    c = pos_q[-1][1] + dc[dir_i]
    tmp_pos_q = (r, c)

    # move
    if _map[r][c] == -1: # 벽에 닿는 경우
        break
    # tail = pos_q.popleft()
    if tmp_pos_q in apples:
        # pos_q.appendleft(tail)
        pos_q.append(tmp_pos_q)
        apples.remove(tmp_pos_q)
    elif tmp_pos_q in pos_q:
        break
    else:
        pos_q.popleft()
        pos_q.append(tmp_pos_q)

    # change direction
    if change_i < len(change) and str(time) == change[change_i][0]:
        if change[change_i][1] == 'L':
            dir_i = (dir_i - 1) % 4
        else: # change[change_i][0] == 'D':
            dir_i = (dir_i + 1) % 4
        change_i += 1
print(time)
