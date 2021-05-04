import sys; input = sys.stdin.readline
from heapq import heappop, heappush

for tc in range(int(input())):
    k = int(input())
    visit = [0] * 1000001
    q_min, q_max = [], []
    for ind in range(k):
        c, i = input().split()
        if c == 'I':
            heappush(q_min, (int(i), ind))
            heappush(q_max, (-int(i), ind))
            visit[ind] = True
        else:  # c == 'D'
            if i == '-1':
                while q_min and not visit[q_min[0][1]]:
                    heappop(q_min)
                if q_min:
                    visit[q_min[0][1]] = False
                    heappop(q_min)
            else:  # i == '1'
                while q_max and not visit[q_max[0][1]]:
                    heappop(q_max)
                if q_max:
                    visit[q_max[0][1]] = False
                    heappop(q_max)
    while q_min and not visit[q_min[0][1]]:
        heappop(q_min)
    while q_max and not visit[q_max[0][1]]:
        heappop(q_max)

    if q_min and q_max:
        print("{} {}".format(-q_max[0][0], q_min[0][0]))
    else:
        print("empty")
