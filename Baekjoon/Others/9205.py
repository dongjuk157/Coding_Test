import sys; input = sys.stdin.readline
from collections import deque

def bfs(graph):
    q = deque()
    q.append(0)
    end = len(graph) - 1
    visit = [-1 for _ in range(len(graph))]
    visit[0] = 0
    while q:
        cur = q.popleft()
        if cur == end:
            return True
        for adj in graph[cur]:
            if visit[adj] != -1:
                continue
            visit[adj] = visit[cur] + 1
            q.append(adj)
    return False

t = int(input())
answer = ''

for tc in range(1, t + 1):
    n = int(input())
    p = [tuple(map(int, input().split())) for _ in range(n + 2)]
    linked_list = [list() for _ in range(n + 2)]
    for i in range(0, n + 2):
        for j in range(i + 1, n + 2):
            x = abs(p[i][0] - p[j][0])
            y = abs(p[i][1] - p[j][1])
            dist = x + y
            if dist <= 1000:
                linked_list[i].append(j)
                linked_list[j].append(i)
    result = bfs(linked_list)
    answer += "happy\n" if result else "sad\n"
print(answer)