# import sys; input = sys.stdin.readline
from collections import deque
def search(start, size, board):
    d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    ret = []
    visit = [[-1 for _ in range(N)] for _ in range(N)]
    visit[start[0]][start[1]] = 0
    q = deque()
    q.append(start)
    while q:
        r, c = q.popleft()
        for i in range(4):
            dr = r + d[i][0]
            dc = c + d[i][1]
            if 0 <= dr < N and 0 <= dc < N:
                # 방문한곳이면 넘어감
                if visit[dr][dc] > -1: continue
                if board[dr][dc]: # 물고기인 경우
                    if board[dr][dc] < size:
                        visit[dr][dc] = visit[r][c] + 1
                        ret.append((dr,dc))
                    elif board[dr][dc] == size:
                        visit[dr][dc] = visit[r][c] + 1
                        q.append((dr, dc))
                else: # 빈 칸인 경우
                    visit[dr][dc] = visit[r][c] + 1
                    q.append((dr, dc))
        if ret: # 같은 거리인 경우 어떻게 확인?
            if q and visit[q[0][0]][q[0][1]] == visit[r][c]:
                continue
            break
    if ret:
        ret.sort(key=lambda x:(x[0], x[1]))
        return (ret[0][0], ret[0][1], visit[ret[0][0]][ret[0][1]])
    return False


N = int(input())
_map = []
pos = [-1, -1]
size, cnt = 2, 0
answer = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    _map.append(tmp)
    for j in range(N):
        if tmp[j] == 9:
            pos[0], pos[1] = i, j

while True:
    exist = search(pos, size, _map)
    if not exist: break
    _map[pos[0]][pos[1]] = 0
    _map[exist[0]][exist[1]] = 9
    pos[0], pos[1] = exist[0], exist[1]
    answer += exist[2]
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0

print(answer)
