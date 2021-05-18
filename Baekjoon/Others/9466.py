import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(node):
    global result
    visit[node] = 1
    cycle.append(node)
    stu = st[node]

    if visit[stu]:
        if stu in cycle:
            result += cycle[cycle.index(stu):]
        return
    dfs(stu)


for tc in range(int(input())):
    n = int(input())
    st = [-1] + list(map(int, input().split()))
    visit = [False] * (n + 1)
    result = []
    for i in range(1, n+1):
        if not visit[i]:
            cycle = []
            dfs(i)


    print(n - len(result))