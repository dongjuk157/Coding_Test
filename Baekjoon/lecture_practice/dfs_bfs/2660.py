import sys
sys.stdin = open('2660_input.txt','r')

from collections import deque
def bfs(queue):
    visited = [0] * (n + 1)
    visited[queue[0]] = 1
    while queue:
        x = queue.popleft()
        for adjacent in link_dict[x]:
            if visited[adjacent]: continue
            queue.append(adjacent)
            visited[adjacent] = visited[x] + 1
    return max(visited)


n = int(input())
link = [[0] * (n + 1) for _ in range(n + 1)]
link_dict = dict(zip(range(n + 1), [[] for i in range(n + 1)]))
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while True:
    i, j = map(int,input().split())
    if i == -1 and j == -1: break
    link_dict[i].append(j)
    link_dict[j].append(i)

min_val = 50
candidate = []
for i in range(1, n + 1):
    q = deque([i])
    score = bfs(q)
    if score < min_val:
        min_val = score
        candidate = [i]
    elif score == min_val:
        candidate.append(i)

print(min_val - 1, len(candidate))
print(*sorted(candidate))


