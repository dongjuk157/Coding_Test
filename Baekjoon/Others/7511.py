# import sys; input = sys.stdin.readline
def find(a, root):
    if root[a] == a:
        return a
    root[a] = find(root[a], root)
    return root[a]


def union(a, b, root):
    x = find(a, root)
    y = find(b, root)
    if x == y:
        return
    root[y] = x
    return


def main():
    answer = []
    for tc in range(int(input())):
        answer.append("Scenario {}:\n".format(tc + 1))
        n = int(input())
        k = int(input())
        root = [i for i in range(n)]
        for _ in range(k):
            a, b = map(int, input().split())
            union(a, b, root)

        m = int(input())
        for _ in range(m):
            u, v = map(int, input().split())
            ru, rv = find(u, root), find(v, root)
            if ru == rv:
                answer.append('1\n')
            else:
                answer.append('0\n')
        answer.append('\n')
    print(''.join(answer))

if __name__ == '__main__':
    main()
