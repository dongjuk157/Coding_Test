import sys; input = sys.stdin.readline
from collections import deque
N, M, K, X = map(int, input().split())
linked_list = [list() for _ in range(N + 1)]
for i in range(M):
    s, e = map(int, input().split())
    linked_list[s].append(e)

visit = [K + 1 for _ in range(N + 1)]
visit[X] = 0

q = deque()
q.append(X)
while q:
    cur = q.popleft()
    for adj in linked_list[cur]:
        if visit[adj] != K and visit[adj] > visit[cur] + 1:
            visit[adj] = visit[cur] + 1
            q.append(adj)

ans = ''
for i in range(N + 1):
    if visit[i] == K:
        ans += str(i)+'\n'

print(ans if ans else -1)