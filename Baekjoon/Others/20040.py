import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def find(a, parent):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a], parent)
    return parent[a]


def union(a, b, parent):
    x = find(a, parent)
    y = find(b, parent)
    if x == y:
        return True
    parent[y] = x
    return False


def main():
    N, M = map(int, input().split())
    parent = [i for i in range(N)]
    for i in range(1, M + 1):
        u, v = map(int, input().split())
        if union(u, v, parent):
            print(i)
            return
    print("0")


if __name__ == '__main__':
    main()
