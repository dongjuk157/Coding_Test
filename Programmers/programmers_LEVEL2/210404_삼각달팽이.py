def solution(n):
    n_list = [[0] * i for i in range(1, 1 + n)]
    max_val = (n ** 2 + n) // 2
    cnt = 0
    x, y = 0, 0

    direction = [(1, 0), (0, 1), (-1, -1)]
    dir_num = 0
    while cnt < max_val:
        cnt += 1
        n_list[x][y] = cnt
        dx = x + direction[dir_num][0]
        dy = y + direction[dir_num][1]
        if 0 <= dx < n and 0 <= dy < len(n_list[dx]) and n_list[dx][dy] == 0:
            x, y = dx, dy
        else:
            dir_num = (dir_num + 1) % 3
            x = x + direction[dir_num][0]
            y = y + direction[dir_num][1]


    answer = []
    for lst in n_list:
        answer.extend(lst)
    return answer

print(solution(4))