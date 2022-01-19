# import sys; input = sys.stdin.readline
def floyd_warshall(n, visit):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                visit[i][j] = min(visit[i][j], visit[i][k] + visit[k][j])
    return visit

def main():
    n, m = map(int, input().split())
    INF = 250 * 250
    visit = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        u, v, b = map(int, input().split())
        visit[u][v] = 0
        visit[v][u] = 0 if b else 1

    for i in range(1, n + 1):
        visit[i][i] = 0
    floyd_warshall(n, visit)

    ans = ''
    for _ in range(int(input())):
        s, e = map(int, input().split())
        ans += '{}\n'.format(visit[s][e])
    print(ans)

if __name__ == '__main__':
    main()