# import sys; input = sys.stdin.readline
R, C, T = map(int, input().split())
room = []
fresher = []
for i in range(R):
    tmp = list(map(int, input().split()))
    room.append(tmp)
    if not fresher:
        for j in range(C):
            if tmp[j] == -1:
                fresher.append((i, j))
                fresher.append((i + 1,j))

# print(*room, sep='\n')
while T > 0:
    T -= 1
    def spread(room):
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        room_tmp = [[0] * C for _ in range(R)]
        # room_tmp[fresher[0][0]][fresher[0][1]] = -1
        # room_tmp[fresher[1][0]][fresher[1][1]] = -1
        # print(dust)
        for r in range(R):
            for c in range(C):
                # r, c = dust[i][j]
                amount = room[r][c]
                spread_amount = amount // 5
                chk_move = 0 # 확산된 방향
                # 최대 네 방향으로 확산
                if spread_amount > 0:
                    for dt in range(4):
                        dr = r + delta[dt][0]
                        dc = c + delta[dt][1]
                        # 인접한 방향에 칸이 없거나 공기청정기가 있으면 확산이 일어나지 않음
                        if dr < 0 or dr >= R or dc < 0 or dc >= C: continue
                        if room[dr][dc] == -1: continue
                        room_tmp[dr][dc] += spread_amount
                        chk_move += 1
                # r, c에 남은 미세먼지 양
                room_tmp[r][c] += amount - spread_amount * chk_move

        return room_tmp
    # print(*room, sep='\n', end='\n\n')
    room = spread(room)
    # print(*room, sep='\n', end='\n\n')

    def clean(room, fresher):
        # 윗부분 반시계방향인데 시계방향으로 확인
        upper = fresher[0]
        # 좌측
        for i in range(upper[0] - 1, -1, -1): # 1, -1,-1 -> 1, 0
            if room[i + 1][0] != -1:
                room[i + 1][0] = room[i][0]
        # 상측
        for i in range(1, C):
            room[0][i - 1] = room[0][i]
        # 우측
        for i in range(1, upper[0] + 1): # 1, 0
            room[i - 1][C - 1] = room[i][C - 1]
        # 하측
        for i in range(C - 2, -1, -1):
            if i != 0:
                room[upper[0]][i + 1] = room[upper[0]][i]
            else:
                room[upper[0]][i + 1] = 0

        # 아래부분 시계방향인데 반시계방향으로 확인
        lower = fresher[1]
        # 좌측
        for i in range(lower[0] + 1, R): # 4,5,6
            if room[i - 1][0] != -1:
                room[i - 1][0] = room[i][0]
        # 하측
        for i in range(1, C):
            room[R - 1][i - 1] = room[R - 1][i]
        # 우측
        for i in range(R - 2, lower[0] - 1, -1):
            room[i + 1][C - 1] = room[i][C - 1]
        # 상측
        for i in range(C - 2, -1, -1):
            if i != 0:
                room[lower[0]][i + 1] = room[lower[0]][i]
            else:
                room[lower[0]][i + 1] = 0

    clean(room, fresher)
    # print(*room, sep='\n', end='\n\n')
def arr_sum():
    ret = 2
    for i in range(R):
        for j in range(C):
            ret += room[i][j]
    return ret

print(arr_sum())

