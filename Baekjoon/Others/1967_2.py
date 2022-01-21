'''
This code is wrong answer.
memory is 128 MB
'''

# import sys; input = sys.stdin.readline
INF = 987654321
def floyd_warshall(linked_array, size):
    # floyd_warshall algorithm
    # find all nodes to all nodes
    for k in range(1, size + 1):
        for i in range(1, size + 1):
            for j in range(1, size + 1):
                linked_array[i][j] = min(
                    linked_array[i][j],
                    linked_array[i][k] + linked_array[k][j]
                )
    # find max value, not INF
    max_val = 0
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if linked_array[i][j] != INF:
                max_val = max(max_val, linked_array[i][j])
    return max_val

def main():
    # 0 input
    N = int(input())
    linked_array = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        linked_array[i][i] = 0
    for _ in range(N - 1):
        a, b, w = map(int, input().split())
        linked_array[a][b] = w
        linked_array[b][a] = w
    # 1 find
    ans = floyd_warshall(linked_array, N)
    # 2 output
    print(ans)

if __name__ == "__main__":
    main()
