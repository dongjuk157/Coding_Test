# import sys; input = sys.stdin.readline

def main():
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    trees = [[[] for _ in range(N + 2)] for _ in range(N + 2)]
    for _ in range(M):
        x, y, z = map(int, input().split())
        trees[x][y].append(z)

    _map = [[5 for _ in range(N + 2)] for _ in range(N + 2)]
    dd = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for _ in range(K):  # for k years
        # spring
        for x in range(1, N + 1):
            for y in range(1, N + 1):
                if not trees[x][y]: continue
                new_tree = []
                dead_tree = 0
                while trees[x][y]:
                    tree_age = trees[x][y].pop()
                    if _map[x][y] >= tree_age:
                        _map[x][y] -= tree_age
                        tree_age += 1
                        new_tree.append(tree_age) # asc
                    else:
                        dead_tree += tree_age // 2
                _map[x][y] += dead_tree
                trees[x][y] = new_tree[::-1] # desc
        # fall
        for x in range(1, N + 1):
            for y in range(1, N + 1):
                if not trees[x][y]: continue
                for tree_age in trees[x][y]:
                    if tree_age % 5: continue  # if age is multiple of 5, breed
                    for d in dd:
                        nx, ny = d[0] + x, d[1] + y
                        if 1 <= nx <= N and 1 <= ny <= N:
                            trees[nx][ny].append(1)
        # winter
        for i in range(N):
            for j in range(N):
                _map[i + 1][j + 1] += A[i][j]

    answer = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if trees[i][j]:
                answer += len(trees[i][j])
    print(answer)


if __name__ == "__main__":
    main()
