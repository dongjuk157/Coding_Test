import sys
sys.stdin = open('.idea/1949_input.txt','r')

for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    k_used_chk = False
    # 3<=n<=8, 1<=k<=5
    _map = []
    max_h = 0
    max_list = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        _map.append(tmp)
        for j in range(n):
            if tmp[j] > max_h:
                max_h = tmp[j]
                max_list = [(i, j)]
            elif tmp[j] == max_h:
                max_list.append((i, j))
    visited = [[0] * n for _ in range(n)]
    #print(max_h, max_list)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    max_val = 0


    def dfs(x, y, index=0):
        global k_used_chk, max_val
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny <n:
                if visited[nx][ny]: continue
                if k_used_chk and _map[nx][ny] >= _map[x][y]: continue
                if _map[nx][ny] >= _map[x][y]:  # and not k_chk: # k를 사용하지 않은경우
                    for i in range(1, k + 1): # 1 ~ K
                        if _map[nx][ny] - i >= _map[x][y]: continue
                        k_used_chk = True
                        _map[nx][ny] -= i
                        visited[nx][ny] = 1
                        dfs(nx, ny, index + 1)
                        visited[nx][ny] = 0
                        _map[nx][ny] += i
                        k_used_chk = False
                else: # if _map[nx][ny] < _map[x][y]:
                    visited[nx][ny] = 1
                    dfs(nx,ny, index + 1)
                    visited[nx][ny] = 0
        tmp_val = index + 1
        if max_val < tmp_val:
            max_val = tmp_val

    for i in range(len(max_list)):
        visited[max_list[i][0]][max_list[i][1]] = 1
        dfs(max_list[i][0],max_list[i][1])
        visited[max_list[i][0]][max_list[i][1]] = 0

    print("#{} {}".format(tc, max_val))

