# import sys; input = sys.stdin.readline
from collections import Counter
def find(x, root, rank):
    if root[x] == x:
        return x
    root[x] = find(root[x], root, rank)
    return root[x]

def union(x, y, root, rank, friend_cost):
    x = find(x, root, rank)
    y = find(y, root, rank)
    if x == y:
        return

    if rank[x] < rank[y]:
        root[x] = y
    else:
        root[y] = x
    if friend_cost[x] < friend_cost[y]:
        friend_cost[y] = friend_cost[x]
    else:
        friend_cost[x] = friend_cost[y]

    if rank[x] == rank[y]:
        rank[x] += 1
    return


def main():
    N, M, K = map(int, input().split())
    A = [0]
    A.extend(map(int, input().split()))
    root = list(range(N + 1))
    rank = [0 for _ in range(N + 1)]
    for _ in range(M):
        v, w = map(int, input().split()) # friend
        union(v, w, root, rank, A)

    # root renew
    for i in range(1, N + 1):
        root[i] = find(i, root, rank)

    # total root node
    total = 0
    for k in Counter(root).keys():
        total += A[k]
    print(total if total <= K else "Oh no")



if __name__ == '__main__':
    main()
