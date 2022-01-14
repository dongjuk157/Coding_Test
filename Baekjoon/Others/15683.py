# import sys; input = sys.stdin.readline
answer = None
N, M = None, None
cctv_list, d_map, r_map = None, None, None
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def check_number():
    ret = 0
    for i in range(N + 2):
        for j in range(M + 2):
            if not d_map[i][j] and not r_map[i][j]:
                ret += 1
    return ret

def renew_map(cctv_num, cctv_direction, val): #d_map
    global N, M, cctv_list, d_map, r_map, d
    for cdr in cctv_direction:
        nr, nc = cctv_list[cctv_num]
        while 0 <= r_map[nr][nc] < 6:
            d_map[nr][nc] += val
            nr += cdr[0]
            nc += cdr[1]

def bt(ind):
    global answer, N, M, cctv_list, d_map, r_map
    if ind == len(cctv_list):
        answer = min(answer, check_number())
        return
    for j in range(4):
        cctv_direction = []
        x, y = cctv_list[ind]
        if r_map[x][y] == 1:
            cctv_direction.append(d[j])
        elif r_map[x][y] == 2:
            cctv_direction.append(d[j])
            cctv_direction.append(d[(j + 2) % 4])
        elif r_map[x][y] == 3:
            cctv_direction.append(d[j])
            cctv_direction.append(d[(j + 1) % 4])
        elif r_map[x][y] == 4:
            cctv_direction.append(d[(j - 1) % 4])
            cctv_direction.append(d[j])
            cctv_direction.append(d[(j + 1) % 4])
        elif r_map[x][y] == 5:
            cctv_direction.extend(d[:])
        renew_map(ind, cctv_direction, 1)

        bt(ind + 1)
        renew_map(ind, cctv_direction, -1)

def main():
    # 0 입력
    global answer, N, M, cctv_list, d_map, r_map
    N, M = map(int, input().split())
    answer = N * M
    cctv_list = []
    d_map = [[-1 for _ in range(M + 2)] for _ in range(N + 2)]
    r_map = []
    r_map.append([-1 for _ in range(M + 2)])
    for i in range(N):
        tmp = list(map(int, input().split()))
        r_map.append([-1] + tmp + [-1])
        for j in range(M):
            if 0 < tmp[j] < 6:
                cctv_list.append((i + 1, j + 1))
                d_map[i+1][j+1] = 0
            elif tmp[j] == 0:
                d_map[i+1][j+1] = 0
    r_map.append([-1 for _ in range(M + 2)])

    # 1 완전탐색 사방
    bt(0)

    # 2 값 출력
    print(answer)


if __name__ == "__main__":
    main()