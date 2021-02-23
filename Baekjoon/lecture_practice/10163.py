

width = height = 101
board = [[0]*width for _ in range(height)]

def cover(number, s_col, s_row, wid, hei):
    for row in range(s_row, s_row + hei):
        for col in range(s_col, s_col + wid):
            board[row][col] = number


n = int(input()) #색종이의 장수를 나타내는 정수 N (1 ≤ N ≤ 100)
for i in range(1, n + 1):
    c, r, w, h = map(int,input().split())
    cover(i, c, r, w, h)

result = [0]*n
for i in range(height):
    for j in range(width):
        if board[i][j]:
            result[board[i][j] - 1] += 1

for _ in result:
    print(_)