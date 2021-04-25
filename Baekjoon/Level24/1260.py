from collections import deque

N, M, V = map(int, input().split())
linked_list = [list() for _ in range(N + 1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    linked_list[n1].append(n2)
    linked_list[n2].append(n1)
for i in range(N):
    linked_list[i].sort()

def dfs(start):
    s = [start]
    visit = [0] * (N + 1)
    while s:
        cur = s[-1]
        if not visit[cur]:
            print(cur, end=' ')
        visit[cur] = 1
        break_chk = False
        for i in range(len(linked_list[cur])):
            if visit[linked_list[cur][i]]: continue
            s.append(linked_list[cur][i])
            break_chk = True
            break
        if break_chk == False:
            s.pop()
    print()


def bfs(start):
    q = deque([start])
    visit = [0] * (N + 1)
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        visit[cur] = 1
        for i in range(len(linked_list[cur])):
            if visit[linked_list[cur][i]]: continue
            visit[linked_list[cur][i]] = 1
            q.append(linked_list[cur][i])
    print()

dfs(V)
bfs(V)