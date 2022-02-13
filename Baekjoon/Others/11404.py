# import sys; input = sys.stdin.readline

def main():
    # init
    INF = 987654321
    n, m = int(input()), int(input())
    cost = [[INF for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        cost[a][b] = min(cost[a][b], c)

    for i in range(n):
        cost[i][i] = 0

    # floyd warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    # print
    answer = []
    for i in range(n):
        for j in range(n):
            if cost[i][j] == INF:
                cost[i][j] = 0
        answer.append(' '.join(map(str, cost[i])))
    print('\n'.join(answer))

if __name__ == '__main__':
    main()
