import sys; input = sys.stdin.readline
from collections import deque

def bfs(q, visit, limit):
    unhappiness = 0
    ind = 0
    flag = False
    while q:
        cur = q.popleft()
        for d in [-1, 1]:
            next = cur + d
            if visit.get(next) is None:
                visit[next] = visit[cur] + 1
                q.append(next)
                unhappiness += visit[next]
                ind += 1
                if ind == limit:
                    flag = True
                    break
        if flag:
            break

    return unhappiness


def main():
    n, k = map(int, input().split())
    visit = {}
    q = deque()
    for i in map(int, input().split()):
        visit[i] = 0
        q.append(i)

    print(bfs(q, visit, k))


if __name__ == "__main__":
    main()
