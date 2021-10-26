import sys; input = sys.stdin.readline
def backtrack(r, c, cnt):
    global answer
    # 1 현재 있는 점이 방문한 점인지 확인
    ch_ord_ind = ord(board[r][c]) - 65
    if alphabet[ch_ord_ind]:
        return
    alphabet[ch_ord_ind] = 1
    if answer < cnt:
        answer = cnt

    # 2 탐색
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            backtrack(nr, nc, cnt+1)

    alphabet[ch_ord_ind] = 0


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
alphabet = [0 for _ in range(26)]
answer = 0
backtrack(0, 0, 1)
print(answer)