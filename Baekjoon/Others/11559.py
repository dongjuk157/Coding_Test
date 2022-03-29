import sys; input = sys.stdin.readline
from collections import deque
d = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # r u l d
def bfs(start_r, start_c, limit):
    global ROW, COL, visit, field
    q = deque()
    q.append((0, start_r, start_c))
    check = 0
    while q:
        dist, r, c = q.popleft()
        if visit[r][c]: continue
        check += 1
        visit[r][c] = 1

        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROW and 0 <= nc < COL:
                if field[r][c] == field[nr][nc]: #시작점과 같으면
                    q.append((dist + 1, nr, nc))
    if check >= limit:
        return True
    return False

def remove_puyo(start_r, start_c):
    global ROW, COL, visit, field
    q = deque()
    q.append((start_r, start_c))
    start_val = field[start_r][start_c]
    while q:
        r, c = q.popleft()
        if not visit[r][c]: continue
        if field[r][c] != start_val: continue
        visit[r][c] = 0
        field[r][c] = '.'
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROW and 0 <= nc < COL:
                q.append((nr, nc))

def gravity():
    global ROW, COL, field
    for c in range(COL):
        cnt_empty = 0
        for r in range(ROW - 1, -1, -1):
            if field[r][c] == '.':
                cnt_empty += 1
            else:
                if cnt_empty:
                    field[r + cnt_empty][c], field[r][c] = field[r][c], '.'


def simulation():
    global ROW, COL, visit, field
    chk = False
    for r in range(ROW - 1, -1, -1):
        for c in range(COL):
            if field[r][c] == '.': continue
            if visit[r][c]: continue
            if bfs(r, c, 4):
                remove_puyo(r, c)
                chk = True
    if chk:
        return 1
    return 0

def main():
    global ROW, COL, visit, field
    ROW, COL = 12, 6
    field = [list(input().rstrip()) for _ in range(ROW)]
    answer = 0
    while True:
        visit = [[0 for _ in range(COL)] for _ in range(ROW)]
        if simulation():
            gravity()
            answer += 1
        else:
            break
    print(answer)


if __name__ == "__main__":
    main()
