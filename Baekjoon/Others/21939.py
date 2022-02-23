import sys; input = sys.stdin.readline
from heapq import heappop, heappush

def main():
    N = int(input())
    min_h, max_h = [], []
    level = {}
    for _ in range(N):
        P, L = map(int, input().split())
        heappush(min_h, (L, P))
        heappush(max_h, (-L, -P))
        if not level.get(P):
            level[P] = 0
        level[P] = L


    M = int(input())
    for _ in range(M):
        c, *args = input().split()
        if c[0] == 'a':
            P, L = map(int, args)
            heappush(min_h, (L, P))
            heappush(max_h, (-L, -P))
            if not level.get(P):
                level[P] = 0
            level[P] = L
        elif c[0] == 's':
            P = int(args[0])
            level[P] = 0
        else: #if c == "recommend"
            x = args[0]
            if x == '1': # max level
                while max_h and level[-max_h[0][1]] != -max_h[0][0]:
                    heappop(max_h)
                print(-max_h[0][1])
            else: # x == -1
                while min_h and level[min_h[0][1]] != min_h[0][0]:
                    heappop(min_h)
                print(min_h[0][1])


if __name__ == "__main__":
    main()
