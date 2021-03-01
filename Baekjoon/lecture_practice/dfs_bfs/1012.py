def dfs(row, col, matrix, visited):
    pass


t = int(input())
for tc in range(1, t + 1):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    delta = [(-1,0),(1,0),(0,-1),(0,1)]
    stack = []
    result = 0
    for r in range(n):
        for c in range(m):
            if field[r][c] and visited[r][c] == 0:
                stack.append((r, c))
                while stack:
                    visit_node = stack[-1]
                    visited[visit_node[0]][visit_node[1]] = 1
                    for dt in delta:
                        dr = visit_node[0] + dt[0]
                        dc = visit_node[1] + dt[1]
                        if 0 <= dr < n and 0 <= dc < m:
                            if field[dr][dc] == 1 and visited[dr][dc] ==0:
                                stack.append((dr,dc))
                                break
                    else:
                        stack.pop()
                result += 1
    print(result)