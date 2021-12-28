# import sys;input = sys.stdin.readline
from collections import deque

# 탐색
def bfs(start, end, size, building):
    q = deque()
    q.append(start)
    visit = [[[0 for k in range(size[2] + 2)] for j in range(size[1] + 2)] for i in range(size[0] + 2)]
    # 0일때 continue 하기위해서 1로 시작, bfs 끝나면 리턴 값에서 1 뺄것
    visit[start[0]][start[1]][start[2]] = 1
    while q:
        l, r, c = q.popleft()
        for ll, rr, cc in [(1, 0, 0), (-1, 0, 0), (0, 1, 0),(0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            dl, dr, dc = l + ll, r + rr, c + cc
            if building[dl][dr][dc] == '#': continue # 벽
            if visit[dl][dr][dc]: continue # 이미 방문한 점
            visit[dl][dr][dc] = visit[l][r][c] + 1
            q.append((dl, dr, dc))
    if visit[end[0]][end[1]][end[2]]:
        return visit[end[0]][end[1]][end[2]] - 1
    return 0

def main():
    while True:
        # 0 입력
        L, R, C = map(int, input().split())
        if (0, 0, 0) == (L, R, C):
            break

        start, end = None, None
        building = []
        for i in range(L + 2):
            tmp_l = []
            for j in range(R + 2):
                if 0 == j or R + 1 == j or 0 == i or L + 1 == i:
                    tmp_r = "#" * (C + 2)
                else:
                    tmp_r = "#" + input() + "#"
                    for k in range(C + 2):
                        if 'S' == tmp_r[k]:
                            start = [i,j,k]
                        elif 'E' == tmp_r[k]:
                            end = [i,j,k]
                tmp_l.append(tmp_r)
            building.append(tmp_l)
            if 0 != i and L + 1 != i:
                _ = input()
        # 탐색
        answer = bfs(start, end, (L, R, C), building)

        # 출력
        if answer:
            print(f"Escaped in {answer} minute(s).")
        else:
            print("Trapped!")

if __name__ == '__main__':
    main()