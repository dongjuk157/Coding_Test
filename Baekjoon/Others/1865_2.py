# import sys; input = sys.stdin.readline
INF = 987654321
def bf(start):
    global N, M, edges, dist

    dist[start] = 0
    for i in range(N):
        for cur, next, cost in edges:
            if dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == N - 1:
                    return True
    return False


def main():
    global N, M, edges, dist
    answer = []
    for tc in range(int(input())):
        N, M, W = map(int, input().split())
        edges = []
        dist = [INF for _ in range(N + 1)]

        for _ in range(M):
            s, e, t = map(int, input().split())
            edges.append((s, e, t))
            edges.append((e, s, t))
        for _ in range(W):
            s, e, t = map(int, input().split())
            edges.append((s, e, -t))

        cycle = bf(1)
        if cycle:
            answer.append("YES")
        else:
            answer.append("NO")
    print("\n".join(answer))


if __name__ == "__main__":
    main()
