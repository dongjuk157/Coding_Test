import sys
sys.stdin = open('1799_input.txt','r')
n = int(input())
matrix = []
pos = []
for i in range(n):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)
    for j in range(n):
        if tmp[j]:
            pos.append((i, j))
visit = [0] * len(pos)
print(pos)

# 조합
max_val = 0
def backtrack(index=0, arr=[]):
    if index == len(pos):
        global max_val
        if max_val < len(arr):
            print(arr)
            max_val = len(arr)
    else:
        for i in range(index, len(pos)):
            if check_bishop(i, arr):
                backtrack(index + 1, arr)
            else:
                backtrack(index + 1, arr + [i])


def check_bishop(index, pos_arr):
    # 대각선 확인 -> abs(x1-x2) == abs(y1-y2)
    for i in range(len(pos_arr)):
        tmp = pos_arr[i]
        if abs(pos[index][0] - pos[tmp][0]) == abs(pos[index][1] - pos[tmp][1]):
            return 1
    return 0

backtrack()
print(max_val)