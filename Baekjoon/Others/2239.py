import sys; input = sys.stdin.readline

def is_correct(value, r, c):
    global sudoku, find_list
    # 1 check row
    for i in range(9):
        if value == sudoku[r][i]:
            return False
    # 2 check col
    for i in range(9):
        if value == sudoku[i][c]:
            return False
    # 3 check square
    for i in range(3):
        for j in range(3):
            rr = 3 * (r // 3) + i
            cc = 3 * (c // 3) + j
            if value == sudoku[rr][cc]:
                return False
    return True

def backtrack(ind):
    global sudoku, find_list, flag
    if flag:
        return
    if ind == len(find_list):
        for i in range(9):
            print(*sudoku[i], sep='')
        flag = True
        return

    r, c = find_list[ind][0], find_list[ind][1]

    for i in range(1, 10):
        if not is_correct(i, r, c):
            continue
        sudoku[r][c] = i
        backtrack(ind + 1)
        sudoku[r][c] = 0


def main():
    global sudoku, find_list, flag
    sudoku = []
    find_list = []
    for i in range(9):
        sudoku.append(list(map(int, input().rstrip())))
        for j in range(9):
            if not sudoku[i][j]:
                find_list.append((i, j))
    flag = False
    backtrack(0)



if __name__ == "__main__":
    main()
