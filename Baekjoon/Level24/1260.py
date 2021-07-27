from collections import deque

N, M, V = map(int, input().split())
linked_list = [list() for _ in range(N + 1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    linked_list[n1].append(n2)
    linked_list[n2].append(n1)

for i in range(N+1):
    linked_list[i].sort()

def dfs(start, visit):
    print(start, end=' ')
    visit[start] = True
    for adj in linked_list[start]:
        if visit[adj]: continue
        dfs(adj, visit)

def bfs(start):
    q = deque()
    q.append(start)
    visit = [False for _ in range(N + 1)]
    while q:
        cur = q.popleft()
        if visit[cur]: continue
        visit[cur] = True
        print(cur, end=' ')
        for adj in linked_list[cur]:
            q.append(adj)


visit = [False for _ in range(N + 1)]
dfs(V, visit)
print()
bfs(V)