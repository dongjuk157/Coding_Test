# import sys; input = sys.stdin.readline
INF = 20_000_000_000

def bf(start):
    global dist, N, M, edges
    dist[start] = 0

    for i in range(N):
        for j in range(M):
            cur, next, cost = edges[j]

            if dist[cur] != INF and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == N - 1:
                    return True
    return False


def main():
    global dist, N, M, edges

    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))

    dist = [INF for _ in range(N + 1)]
    cycle = bf(1)
    if cycle:
        print("-1")
    else:
        for i in range(2, N+1):
            if dist[i] == INF:
                print("-1")
            else:
                print(dist[i])


if __name__ == "__main__":
    main()
