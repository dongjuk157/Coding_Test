# import sys; input = sys.stdin.readline
from collections import deque
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def find_answer(arr, size):
    real_size = 2 ** size
    total, big_amount = 0, 0
    visit = [[0 for _ in range(real_size)] for _ in range(real_size)]
    for i in range(real_size):
        for j in range(real_size):
            if not arr[i][j]: continue
            if visit[i][j]: continue
            amount = 0 # find big amount
            # bfs
            q = deque()
            q.append((i, j))
            while q:
                r, c = q.popleft()
                if visit[r][c]: continue
                visit[r][c] = 1
                total += arr[r][c] # find total amount
                amount += 1 # find big amount
                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < real_size and 0 <= nc < real_size:
                        if arr[nr][nc]:
                            q.append((nr, nc))
            big_amount = max(big_amount, amount) # find big amount

    return total, big_amount

def rotate_grid(start_r, start_c, grid_size, arr):
    ret = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for r in range(grid_size):
        for c in range(grid_size):
            before_r, before_c = start_r + r, start_c + c
            ret[c][grid_size - 1 - r] = arr[before_r][before_c]
    return ret

def main():
    # input
    N, Q = map(int, input().split())
    arr_size = 2 ** N
    A = [list(map(int, input().split())) for _ in range(arr_size)]
    L_list = list(map(int, input().split()))
    for L in L_list:
        if L:
            # Rotate 90 degrees clockwise, each grid's size 2 ** L
            grid_size = 2 ** L
            for i in range(0, arr_size, grid_size):
                for j in range(0, arr_size, grid_size):
                    # rotate arr
                    tmp = rotate_grid(i, j, grid_size, A)
                    # copy rotate arr into arr
                    for tmp_i in range(grid_size):
                        for tmp_j in range(grid_size):
                            A[i+tmp_i][j+tmp_j] = tmp[tmp_i][tmp_j]

        # if ice's amount less than 3, melting
        melting = []
        for i in range(arr_size):
            for j in range(arr_size):
                if not A[i][j]: continue
                adj = 0
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < arr_size and 0 <= nj < arr_size:
                        if A[ni][nj]:
                            adj += 1
                if adj < 3:
                    melting.append((i, j))
        while melting:
            i, j = melting.pop()
            A[i][j] -= 1

    # output
    print(*find_answer(A, N), sep='\n')


if __name__ == "__main__":
    main()
