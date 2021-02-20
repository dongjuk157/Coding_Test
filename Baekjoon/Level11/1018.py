def change_color(matrix, index_row, index_col):
    board1 = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB',]
    board2 = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW',]
    result1 = 0
    result2 = 0
    for r in range(8):
        for c in range(8):
            if not board1[r][c] == matrix[index_row + r][index_col + c]:
                result1 += 1
            if not board2[r][c] == matrix[index_row + r][index_col + c]:
                result2 += 1
    return min(result1, result2)

n, m = map(int, input().split())
board = [input() for _ in range(n)]
result = 64
for i in range(n+1-8):
    for j in range(m+1-8):
        tmp = change_color(board, i, j)
        if result > tmp:
            result = tmp
print(result)



