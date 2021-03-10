n = int(input())

matrix = [[0] * n for _ in range(n)]
result = 0
visited = [0] * n

def backtrack(index, arr=[]):
    if index == n:
        global result
        result += 1
        return
    else:
        for i in range(n): # 한줄에서 하나씩만 보면 됨
            if visited[i]: continue
            matrix[index][i] = 1
            if check_queen(index, i, arr): continue

            visited[i] = 1
            backtrack(index + 1, arr + [i])
            visited[i] = 0
#            matrix[index][i] = 0

def check_queen(x, y, arr):
    for i in range(len(arr)):
        if abs(i - x) == abs(arr[i] - y):
            return 1
    return 0

backtrack(0)
print(result)