import sys; input = sys.stdin.readline
def sum_arr(array):
    ret = 0
    for i in range(N):
        for j in range(M):
            ret += array[i][j]
    return ret
def backtrack(arr, total=0, ind=0):
    global max_val
    if ind == 3:
        if max_val < total:
            max_val = total
        return
    for i in range(3):
        dr = arr[-1][0] + delta[i][0]
        dc = arr[-1][1] + delta[i][1]
        if 0 <= dr < N and 0 <= dc< M:
            if visit[dr][dc]: continue
            visit[dr][dc] = 1
            backtrack(arr+[(dr, dc)],total+matrix[dr][dc], ind + 1)
            visit[dr][dc] = 0


N, M = map(int, input().rstrip().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
max_val = 0
delta = [(1, 0), (0, -1), (0, 1)]
visit = [[0] * M for _ in range(N)]
plus = [[(0,0),(0,1),(0,2),(1,1)],[(0,1),(1,0),(1,1),(1,2)], [(1,0),(0,1),(1,1),(2,1)],[(0,0),(1,0),(2,0),(1,1)]]
for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        backtrack([(i,j)], matrix[i][j])
        visit[i][j] = 0
        for k in range(4):
            tmp = 0
            for l in range(4):
                dr = i + plus[k][l][0]
                dc = j + plus[k][l][1]
                if 0<= dr < N and 0<= dc < M:
                    tmp += matrix[dr][dc]
            else:
                max_val = max(max_val,tmp)
print(max_val)