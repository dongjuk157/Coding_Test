import sys
input = sys.stdin.readline
sudoku = []
zero_list = []
for i in range(9):
    tmp = list(map(int, input().split()))
    sudoku.append(tmp)
    for j in range(9):
        if tmp[j]: continue
        zero_list.append((i,j))

def backtrack(index):
    if index == len(zero_list):
        return 1
    else:
        x, y = zero_list[index]
        for i in range(1, 10):
            if check(x, y, i): continue
            sudoku[x][y] = i
            if backtrack(index + 1): return 1
            sudoku[x][y] = 0

def check(x, y, number):
    for i in range(9):
        if sudoku[x][i] == number or sudoku[i][y] == number:
            return True

    #3 3*3 block
    for i in range(3):
        for j in range(3):
            tmp_x = (x // 3)*3 + i
            tmp_y = (y // 3)*3 + j
            if sudoku[tmp_x][tmp_y] == number:
                return True
    return False

backtrack(0)

for i in range(9):
    print(*sudoku[i])



