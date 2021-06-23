def max_check(arr, H, W):
    cnt = 0
    for r in range(H - 1):
        for c in range(W - 1):
            if two_by_two_check(arr, r, c):
                two_by_two_change(arr, r, c)
                cnt += 1
    return cnt

def two_by_two_check(arr, row, col):
    if arr[row][col] or arr[row+1][col] or arr[row][col+1] or arr[row+1][col+1]:
        return False
    return True

def two_by_two_change(arr, row, col, value):
    arr[row][col] = arr[row+1][col] = arr[row][col+1] = arr[row+1][col+1] = value

def dfs(arr, row=0, col=0, chips=0):
    global result
    if col >= W - 1:
        if row >= H - 2:
            if result < chips:
                result = chips
            return
        else:
            dfs(arr, row + 1, 0, chips)

    if 0 <= row < H-1 and 0 <= col < W-1:
        if not visit[row][col] and two_by_two_check(arr, row, col):
            two_by_two_change(arr, row, col, 1)
            dfs(arr, row, col+2, chips + 1)
            two_by_two_change(arr, row, col, 0)
        dfs(arr, row, col+1, chips)


T = int(input())
for tc in range(1, T+1):
    result = 0
    H, W = map(int, input().split())
    wafer = [0]
    wafer = [list(map(int, input().split())) for _ in range(H)]
    visit = [[wafer[r][c] for c in range(W)] for r in range(H)]
    dfs(wafer)
    print(f"#{tc} {result}")