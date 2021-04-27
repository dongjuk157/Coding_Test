import sys
input = sys.stdin.readline
from collections import deque

K = int(input())
for tc in range(K):
    V, E = map(int, input().split())
    # 인접 리스트 
    link_arr = [list() for _ in range(V + 1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        link_arr[n1].append(n2)
        link_arr[n2].append(n1)
    # 방문 확인
    visit = [0] * (V + 1)

    def bfs(start):
        q = deque()
        q.append(start)
        visit[start] = 1
        while q:
            cur = q.popleft()
            for i in range(len(link_arr[cur])):
                adj = link_arr[cur][i]
                if visit[adj]:
                    if (visit[cur] == 2 and visit[adj] == 2) or (visit[cur] == 1 and visit[adj] == 1):
                        return False
                    else:
                        continue
                if visit[cur] % 2 : # 홀수인경우
                    visit[adj] = 2
                else:
                    visit[adj] = 1
                q.append(adj)
        return True
    result = True
    for i in range(1, V + 1):
        if visit[i]: continue
        result = bfs(i)
        if not result:
            break

    print("YES" if result else "NO")
