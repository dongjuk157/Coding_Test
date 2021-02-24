import sys
sys.stdin = open('./.idea/1211_input.txt','r')
# 가장 짧은 이동 거리를 갖는 시작점 x를 반환하는 코드
# (복수 개인 경우 가장 큰 x좌표)
for _ in range(10):
    tc = int(input())
    row, col = 100, 100
    matrix = [list(map(int, input().split())) for i in range(100)]

    start_index = []
    for i in range(col):
        if matrix[0][i]==1:
            start_index.append(i)

    distance = []
    for index in start_index:
        r, c = 0, index
        distance_tmp = 0
        while r < row : # 99에 도착하면 끝
            if 0 <= c-1 < col and matrix[r][c-1]:
                while c > 0 and matrix[r][c-1]:
                    c -= 1
                    distance_tmp += 1
            elif 0 <= c + 1 < col and matrix[r][c+1]:
                while c < 99 and matrix[r][c+1]:
                    c += 1
                    distance_tmp += 1
            r += 1
            distance_tmp += 1
        distance.append(distance_tmp)
    min_ind, min_val = 0, row*col
    for ind, val in enumerate(distance):
        if min_val >= val:
            min_val = val
            min_ind = ind

    print(f"#{tc} {start_index[min_ind]}")




