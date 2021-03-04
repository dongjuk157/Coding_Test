def find_adjacent(matrix, node):
    # node = (row, col)
    _list = []
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)] #상하좌우
    for dt in delta:
        tmp_row = node[0] + dt[0]
        tmp_col = node[1] + dt[1]
        if 0 <= tmp_row < len(matrix) and 0 <= tmp_col < len(matrix):
            if matrix[tmp_row][tmp_col] == '1':
                _list.append((tmp_row, tmp_col))
    return _list


n = int(input())
apart_complex = [input() for _ in range(n)]
visited = [[0]*n for _ in range(n)]
stack = []
num_of_apart = []
count = 1
danji = 1
for r in range(n):
    for c in range(n):
        if apart_complex[r][c] == '1' and visited[r][c] == 0:
            #print(r,c)
            stack.append((r, c))
            while stack:
                visit_node = stack[-1]
                visited[visit_node[0]][visit_node[1]] = danji
                adjacent_graph = find_adjacent(apart_complex, visit_node)
                #print(adjacent_graph)
                for adjacent in adjacent_graph:
                    if not visited[adjacent[0]][adjacent[1]]:
                        count += 1
                        stack.append(adjacent)
                        break
                else:
                    stack.pop()
            else:
                num_of_apart.append(count)
                count = 1
                danji += 1
else:
    danji -= 1

print(danji)
for num in sorted(num_of_apart):
    print(num)

