import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def find(a, p):
    if a == p[a]:
        return a
    p[a] = find(a, p)
    return a

def union(a, b, p):
    a = find(a, p)
    b = find(b, p)
    if a <= b:
        p[a] = b
    else:
        p[b] = a


def main():
    n, m = map(int, input().split())
    answer = []
    parent = [i for i in range(n + 1)]
    for _ in range(m):
        c, a, b = map(int, input().split())
        if c: # answer(find)
            ret = ()
            if parent[a] == parent[b]:
                answer.append("YES")
            else:
                answer.append("NO")
        else: # union & find
            union(a, b, parent)
    print("\n".join(answer))

if __name__ == "__main__":
    main()
