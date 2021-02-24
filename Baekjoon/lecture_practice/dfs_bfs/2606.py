node = int(input())
vertex = int(input())
graph = [list() for _ in range(node + 1)]
for _ in range(vertex):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (node + 1)
stack = [1]   # 1번 컴퓨터 부터 시작
while stack:  # stack 이 비어있는 경우에 끝남
    visit_node = stack[-1]
    visited[visit_node] = 1
    for adjacent in graph[visit_node]:
        if not visited[adjacent]:
            stack.append(adjacent)
            break
    else:
        stack.pop()
print(sum(visited)-1)
