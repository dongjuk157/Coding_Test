def dfs1(row, col, matrix,
         visited):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    stack = [(row, col)]
    while stack:
        visit_node = stack[-1]
        visited[visit_node[0]][visit_node[1]] = 1
        adjacent = []
        for dt in delta:
            if 0 <= visit_node[0] + dt[0] < len(matrix) and 0 <= visit_node[1] + dt[1] < len(matrix):
                if matrix[visit_node[0]][visit_node[1]] == matrix[visit_node[0]+dt[0]][visit_node[1]+dt[1]]:
                    if not visited[visit_node[0]+dt[0]][visit_node[1]+dt[1]]:
                        adjacent.append((visit_node[0] + dt[0], visit_node[1] + dt[1]))
        for adj in adjacent:
            stack.append(adj)
            break
        else:
            stack.pop()


def dfs2(row, col, matrix, visited):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    stack = [(row, col)]
    while stack:
        visit_node = stack[-1]
        visited[visit_node[0]][visit_node[1]] = 1
        adjacent = []
        for dt in delta:
            if 0 <= visit_node[0] + dt[0] < len(matrix) and 0 <= visit_node[1] + dt[1] < len(matrix):
                if matrix[visit_node[0]][visit_node[1]] == matrix[visit_node[0] + dt[0]][visit_node[1] + dt[1]]:
                    if not visited[visit_node[0] + dt[0]][visit_node[1] + dt[1]]:
                        adjacent.append((visit_node[0] + dt[0], visit_node[1] + dt[1]))
                elif matrix[visit_node[0]][visit_node[1]] == 'R' and matrix[visit_node[0] + dt[0]][visit_node[1] + dt[1]] == "G":
                    if not visited[visit_node[0] + dt[0]][visit_node[1] + dt[1]]:
                        adjacent.append((visit_node[0] + dt[0], visit_node[1] + dt[1]))
                elif matrix[visit_node[0]][visit_node[1]] == 'G' and matrix[visit_node[0] + dt[0]][visit_node[1] + dt[1]] == "R":
                    if not visited[visit_node[0] + dt[0]][visit_node[1] + dt[1]]:
                        adjacent.append((visit_node[0] + dt[0], visit_node[1] + dt[1]))
        for adj in adjacent:
            stack.append(adj)
            break
        else:
            stack.pop()


n = int(input())
picture = [input() for _ in range(n)]

visited1 = [[0]*n for _ in range(n)]
visited2 = [[0]*n for _ in range(n)]
result1 = 0   # 정상인
result2 = 0  # 적녹색약

for i in range(n):
    for j in range(n):
        # 정상
        if not visited1[i][j]:
            dfs1(i, j, picture, visited1)
            result1 += 1

        # 적녹색약
        if not visited2[i][j]:
            dfs2(i, j, picture, visited2)
            result2 += 1


print(result1, result2)