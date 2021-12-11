for tc in range(1, int(input()) + 1):
    N = int(input())
    matrix = []
    visited = [[-1] * N for _ in range(N)] # core:0 visit:1, not_visit:-1
    core = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        matrix.append(tmp)
        for j in range(N):
            if tmp[j]:
                core.append((i, j))
                visited[i][j] = 0

    linked_core = 0
    linked_line = 0
    electric_line = [list() for i in range(len(core))]
    # 1 모든 core에서 최소 거리 확인
    for index in range(len(core)):
        tmp = []
        tmp.append(core[index][0])                  # 상
        tmp.append((len(matrix) - core[index][0]) - 1)    # 하
        tmp.append(core[index][1])                  # 좌
        tmp.append((len(matrix) - core[index][1]) - 1)    # 우
        electric_line[index] = tmp

    def backtrack(visit, index=0, total_line=0, total_core=0):
        if index == len(core):
            global linked_line, linked_core
            if linked_core < total_core:
                linked_core = total_core
                linked_line = total_line
                # print(total_core, total_line)
                # print(*visit, sep='\n', end='\n\n')

            elif linked_core == total_core:
                if linked_line > total_line:
                    linked_line = total_line
                    # print(total_core, total_line)
                    # print(*visit, sep='\n', end='\n\n')

        else:# 방향 0,1,2,3, : 상하좌우
            cnt = 0
            if core[index][0] == 0 or core[index][0] == len(matrix) - 1 or\
                    core[index][1] == 0 or core[index][1] == len(matrix) - 1:
                backtrack(visit, index + 1, total_line, total_core + 1)
            else:
                for i in range(4):
                    if find_cross(core[index][0], core[index][1], i, visit):
                        cnt += 1
                        continue
                    tmp_visit = [vs[:] for vs in visit]
                    paint(core[index][0], core[index][1], i, tmp_visit)
                    tmp1 = electric_line[index][i]
                    backtrack(tmp_visit, index + 1, total_line + electric_line[index][i], total_core + 1)

                if cnt == 4:
                    backtrack(visit, index + 1, total_line, total_core)


    def find_cross(x, y, direction, visit):
        # cross 하는지만 확인
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dx = x + delta[direction][0]
        dy = y + delta[direction][1]
        while 0 <= dx < len(visit) and 0 <= dy < len(visit):
            if visit[dx][dy] > -1:
                return True
            dx += delta[direction][0]
            dy += delta[direction][1]
        return False

    def paint(x, y, direction, visit):
        # 해당 방향으로 그림
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dx = x + delta[direction][0]
        dy = y + delta[direction][1]
        while 0 <= dx < len(visit) and 0 <= dy < len(visit):
            visit[dx][dy] = 1
            dx += delta[direction][0]
            dy += delta[direction][1]


    backtrack(visited)
    print("#{} {}".format(tc, linked_line))
