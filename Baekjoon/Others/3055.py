from collections import deque
# import sys; input = sys.stdin.readline
# 1 입력
R, C = map(int, input().split())
_map = [['X' for _ in range(C + 2)] for _ in range(R + 2)]
water_pos = deque()
sonic_pos = deque()
end = None
for i in range(R):
    tmp = list(input())
    for j in range(C):
        _map[i + 1][j + 1] = tmp[j]
        if tmp[j] == 'D':
            end = (i + 1, j + 1)
        elif tmp[j] == 'S':
            sonic_pos.append((i + 1, j + 1))
        elif tmp[j] == '*':
            water_pos.append((i + 1, j + 1))

# 2 반복문
sonic = [[-1 for _ in range(C+2)] for _ in range(R+2)]
water = [[-1 for _ in range(C+2)] for _ in range(R+2)]
sonic[sonic_pos[0][0]][sonic_pos[0][1]] = 0
for x, y in water_pos:
    water[x][y] = 0

while True:
    def bfs_step(start_array, visited, opposit_visited, isSonic):
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ret = deque()
        while start_array:
            cur_x, cur_y = start_array.popleft()
            for x, y in delta:
                dx = cur_x + x
                dy = cur_y + y
                if visited[dx][dy] != -1: continue
                if _map[dx][dy] == 'X': continue
                if isSonic and opposit_visited[dx][dy] != -1: continue
                if not isSonic and _map[dx][dy] == 'D': continue
                visited[dx][dy] = visited[cur_x][cur_y] + 1
                ret.append((dx, dy))
        return ret
    # 2-1 고슴도치 이동
    tmp_sonic = bfs_step(sonic_pos, sonic, water, True)
    # 2-2 물이동
    tmp_water = bfs_step(water_pos, water, sonic, False)
    # 2-3 도착 불가능
    if not tmp_sonic and not tmp_water:
        print('KAKTUS')
        break
    # 2-4 도착 가능
    if sonic[end[0]][end[1]] != -1:
        print(sonic[end[0]][end[1]])
        break
    sonic_pos = deque(set(tmp_sonic)-set(tmp_water))
    water_pos = tmp_water

# print("hello, world")