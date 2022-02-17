import sys; input = sys.stdin.readline
INF = 987654321

def floydWashall(linked_road):
    V = len(linked_road) - 1 
    # distances = [[INF for _ in range(V + 1)] for _ in range(V + 1)]

    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                linked_road[i][j] = min(
                    linked_road[i][j],
                    linked_road[i][k] + linked_road[k][j]     
                )
    
    return


def main():
    # 0 입력
    V, E = map(int, input().split())
    linked_road = [[INF for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        linked_road[a][b] = c
    for i in range(1, V + 1):
        linked_road[i][i] = 0
     
    # 1 모든 도시간 최소 거리 탐색
    floydWashall(linked_road)
    
    # 2 사이클 탐색
    answer = INF
    for i in range(1, V + 1):
        for j in range(i + 1, V + 1):
            answer = min(answer, linked_road[i][j] + linked_road[j][i])
    # 3 최소 도로 길이 출력
    if answer >= INF:
        answer = -1
    print(answer)

if __name__ == "__main__":
    main()
