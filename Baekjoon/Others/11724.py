N, M = map(int, input().split())
# 방향 없는 그래프
G = [list() for _ in range(N + 1)]
visit = [1] + [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

result = 0
for i in range(1, N + 1):
    if visit[i]: continue
    def dfs(start):
        s = [start]
        while s:
            cur = s[-1]
            # if visit[cur]: continue
            visit[cur] = 1
            for adj in G[cur]:
                if visit[adj]: continue
                s.append(adj)
                break
            else:
                s.pop()
    result += 1
    dfs(i)
print(result)




