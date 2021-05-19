# import sys; input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
n = int(input())
nums = [0]+[int(input()) for _ in range(n)]
visit = [False] * (n+1)
finish = [False] * (n+1)
result = []


def dfs(node):
    global result
    visit[node] = True
    cycle.append(node)
    next = nums[node]
    if visit[next]:
        if next in cycle:
            ind = cycle.index(next)
            for i in range(ind,len(cycle)):
                num = cycle[i]
                if not finish[num]:
                    finish[num] = True
        return
    dfs(nums[node])

for i in range(1, n + 1):
    if not visit[i]:
        cycle = []
        dfs(i)
print(sum(finish))
for i in range(len(finish)):
    if finish[i]:
        print(i)