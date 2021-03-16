from copy import deepcopy

def backtrack(arr, index=5,
              dir_arr=[]):

    if index == 0:
        global max_val
        tmp = findmax(arr)
        if max_val < tmp:
            max_val = tmp
        return
    else:
        for i in range(4):
            tmp_arr = deepcopy(arr)
            tmp_arr = add_box(tmp_arr, i)
            backtrack(tmp_arr, index - 1, dir_arr+[i])

def add_box(arr, direction): # direction 0123: 상우하좌(시계방향)
    arr = gravity(arr, direction)
    #print(*arr, sep='\n', end='\n\n')
    if direction == 0: # 위
        for i in range(len(arr) - 1):
            for j in range(len(arr)):
                if arr[i][j] and arr[i][j] == arr[i + 1][j]:
                    arr[i][j] *= 2
                    arr[i + 1][j] = 0
    elif direction == 1: # 오른쪽
        for i in range(len(arr)):
            for j in range(len(arr) - 1, 0, -1):
                if arr[i][j] and arr[i][j] == arr[i][j - 1]:
                    arr[i][j] *= 2
                    arr[i][j - 1] = 0
    elif direction == 2: # 아래
        for i in range(len(arr) - 1, 0, -1):
            for j in range(len(arr)):
                if arr[i][j] and arr[i][j] == arr[i - 1][j]:
                    arr[i][j] *= 2
                    arr[i - 1][j] = 0
    elif direction == 3: # 왼쪽
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr[i][j] and arr[i][j] == arr[i][j + 1]:
                    arr[i][j] *= 2
                    arr[i][j + 1] = 0
    arr = gravity(arr, direction)
    #print(*arr, sep='\n', end='\n\n')
    return arr

def gravity(arr, direction):
    length = len(arr)
    tmp_arr = []
    if direction == 0 or direction == 2:  # 위아래
        for i in range(len(arr)):
            tmp = []
            for j in range(len(arr)):
                if arr[j][i]:
                    tmp.append(arr[j][i])
            if len(tmp) < length:
                if direction == 0:      # 위
                    tmp = tmp + [0] * (length - len(tmp))
                elif direction == 2:    # 아래
                    tmp = [0] * (length - len(tmp)) + tmp
            tmp_arr.append(tmp)
        for i in range(1, length): # 1 2 3 4
            for j in range(i): # 0 01 012 0123
                tmp_arr[i][j], tmp_arr[j][i] = tmp_arr[j][i], tmp_arr[i][j]
    elif direction == 1 or direction == 3:  # 오른쪽 왼쪽
        for i in range(len(arr)):
            tmp = []
            for j in range(len(arr)):
                if arr[i][j]:
                    tmp.append(arr[i][j])
            if len(tmp) < length:
                if direction == 1:  # 오른쪽
                    tmp = [0] * (length - len(tmp)) + tmp
                elif direction == 3:  # 왼쪽
                    tmp = tmp + [0] * (length - len(tmp))
            tmp_arr.append(tmp)

    return tmp_arr

def findmax(arr):
    val = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if val < arr[i][j]:
                val = arr[i][j]
    return val


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_val = 0
backtrack(matrix)
print(max_val)