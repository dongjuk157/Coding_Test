# import sys; sys.stdin = open("swea_5650.txt", "r")

def change_direction(d, block):
    # d: 0, 1, 2, 3 => r, d, l, u
    ret = None
    if block == 1:
        if d == 2:       ret = 3
        elif d == 1:     ret = 0
        else:            ret = (d + 2) % 4
    elif block == 2:
        if d == 2:       ret = 1
        elif d == 3:     ret = 0
        else:            ret = (d + 2) % 4
    elif block == 3:
        if d == 0:       ret = 1
        elif d == 3:     ret = 2
        else:            ret = (d + 2) % 4
    elif block == 4:
        if d == 0:       ret = 3
        elif d == 1:     ret = 2
        else:            ret = (d + 2) % 4
    elif block == 5:
        ret = (d + 2) % 4
    else:
        ret = d
    return ret

def main():
    T = int(input())
    for tc in range(1, T + 1):
        # 0 initiate
        answer = 0
        N = int(input())
        wormhole = dict()
        _map = []

        dr = [0, 1, 0, -1]  # clockwise
        dc = [1, 0, -1, 0]
        for i in range(N):
            _map.append(list(map(int, input().split())))
            for j in range(N):
                if 6 <= _map[i][j] <= 10:
                    if not wormhole.get(_map[i][j]):
                        wormhole[_map[i][j]] = (i, j)
                    else:
                        wormhole[(i, j)] = wormhole[_map[i][j]]
                        wormhole[wormhole[_map[i][j]]] = (i, j)
        # 1 simulate
        for i in range(N):
            for j in range(N):
                if _map[i][j]:
                    # 아무것도 없는 블록만 실행
                    continue
                for d in range(4):
                    r, c = i, j
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 > nr or nr >= N or 0 > nc or nc >= N:
                        # 처음 부터 벗어 나는 방향은 중복 되는 방향임
                        continue
                    if _map[nr][nc] <= 0:
                        # 해당 방향이 비어 있으면 중복 되는 방향
                        # 블랙홀이면 score 0
                        continue

                    # 진행 방향에 블록이 있는 경우 실행
                    score = 0
                    while True:
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < N and 0 <= nc < N:
                            if _map[nr][nc] == -1 or (nr == i and nc == j):
                                # blackhole or starting point
                                break
                            if not _map[nr][nc]:
                                # empty space
                                r, c = nr, nc
                                continue

                            if 1 <= _map[nr][nc] <= 5:
                                # reflecting block
                                # if reflecting, score up
                                nd = change_direction(d, _map[nr][nc])
                                if abs(nd - d) == 2 and r == i and c == j:
                                    break
                                score += 1
                                r, c = nr, nc
                                d = nd
                                continue

                            elif 6 <= _map[nr][nc] <= 10:
                                # wormhole
                                r, c = wormhole[(nr, nc)]
                        else:
                            # if outside, change direction
                            if r == i and c == j:
                                break

                            d = (d + 2) % 4
                            score += 1
                            if 0 < _map[r][c] <= 5:
                                d = change_direction(d, _map[r][c])
                                score += 1
                            elif 5 < _map[r][c] <= 10:
                                r, c = wormhole[(r, c)]

                    answer = max(answer, score)

        # 2 output
        print(f"#{tc} {answer}")


if __name__ == "__main__":
    main()
