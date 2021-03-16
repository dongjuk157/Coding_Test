import sys
sys.stdin = open('.idea/4013_input.txt','r')

from collections import deque

for tc in range(1, int(input()) + 1):
    k = int(input())
    magnet = [0] + [deque(list(map(int, input().split()))) for _ in range(4)]
    # 접점  (1-2,2-6),(2-2,3-6),(3-2,4-6)
    # N극 0, S극 1
    # 시계방향 1, 반시계 -1
    for i in range(k):
        rot_dir = [-1] * 5  # 극성이 다르면 반대방향으로 돌아야됨 [0]은 사용하지 않음
        broken = [1] * 3  # 12,23,34
        mg, direction = map(int, input().split())
        rot_dir[mg] = direction

        if magnet[1][2] == magnet[2][6]:
            broken[0] = 0
        if magnet[2][2] == magnet[3][6]:
            broken[1] = 0
        if magnet[3][2] == magnet[4][6]:
            broken[2] = 0
        # print(broken) # broken = 1 0 1
        for idx in range(2): # 양방향으로 탐색
            if idx:  # 왼쪽 탐색
                mg_tmp = mg - 1
                while 0 < mg_tmp:
                    tmp1 = rot_dir[mg_tmp + 1] * broken[mg_tmp - 1]
                    rot_dir[mg_tmp] = rot_dir[mg_tmp + 1] * broken[mg_tmp - 1] * (-1)
                    mg_tmp -= 1
            else:    # 오른쪽 탐색
                mg_tmp = mg + 1
                while mg_tmp <= 4:
                    rot_dir[mg_tmp] = rot_dir[mg_tmp - 1] * broken[mg_tmp - 2] * (-1)
                    mg_tmp += 1
        # print(rot_dir)
        def rotate():
            for i in range(1,5):
                if rot_dir[i] == 1:
                    tmp = magnet[i].pop()
                    magnet[i].appendleft(tmp)
                elif rot_dir[i] == -1:
                    tmp = magnet[i].popleft()
                    magnet[i].append(tmp)
        rotate()
    result = 0
    for i in range(1,5):
        result += magnet[i][0] * (1 << (i-1))

    print("#{} {}".format(tc, result))