import sys; input = sys.stdin.readline
from heapq import heappop, heappush
def main():
    N = int(input())
    lst = sorted([tuple(map(int, input().split())) for _ in range(N)])

    answer = []
    for s, t in lst:
        if not answer:
            heappush(answer, t)
        else:
            if s >= answer[0]:
                heappop(answer)
                heappush(answer, t)
            else:
                heappush(answer, t)
    print(len(answer))

if __name__ == "__main__":
    main()
