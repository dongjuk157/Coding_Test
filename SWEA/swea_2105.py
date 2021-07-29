import sys
sys.stdin = open("swea_2105.txt", "r")
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    answer = -1
    # [1,1], [1,2],[2,1], ~, [1,19], ~ ,[19,1] 2~ 20
    boundery = []
    for k in range(2, 21):
        for i in range(k):
            if i and k - i:
                boundery.append((i,k-i))

    for l, r in boundery:
        for i in range(N):
            for j in range(N):
                def check(i, j, l, r):
                    pos_r, pos_c_l, pos_c_r = i, j, j
                    l_dir, r_dir = -1, 1
                    loop_set = set()
                    loop_set.add(matrix[i][j])
                    while True:
                        pos_r += 1
                        pos_c_l += l_dir
                        pos_c_r += r_dir
                        if not (0 <= pos_c_l< N and 0 <= pos_c_r < N and 0<=pos_r<N):
                            return -1
                        l -= 1
                        r -= 1
                        if not l:
                            l_dir = -l_dir
                        if not r:
                            r_dir = -r_dir

                        if pos_c_l == pos_c_r:
                            if matrix[pos_r][pos_c_l] not in loop_set:
                                loop_set.add(matrix[pos_r][pos_c_l])
                                break


                        if matrix[pos_r][pos_c_l] in loop_set:
                            return -1
                        loop_set.add(matrix[pos_r][pos_c_l])

                        if matrix[pos_r][pos_c_r] in loop_set:
                            return -1
                        loop_set.add(matrix[pos_r][pos_c_r])
                    return len(loop_set)
                tmp = check(i, j, l, r)
                if answer < tmp:
                    answer = tmp

    print("#{} {}".format(tc, answer))