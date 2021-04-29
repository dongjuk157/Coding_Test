# import sys
# input = sys.stdin.readline

from collections import deque
N = int(input())
s, e = map(int, input().split())
link_arr = [list() for _ in range(N + 1)]
M = int(input())
for _ in range(M):
    n1, n2 = map(int, input().split())
    link_arr[n1].append(n2)
    link_arr[n2].append(n1)

visit = [-1] * (N + 1)
q = deque()
q.append(s)
visit[s] = 0
while q:
    cur = q.popleft()
    if cur == e:
        break
    for adj in link_arr[cur]:
        if visit[adj] > -1: continue
        visit[adj] = visit[cur] + 1
        q.append(adj)

print(visit[e])