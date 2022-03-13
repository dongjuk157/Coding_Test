# import sys; input = sys.stdin.readline
from bisect import bisect_left

def index(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1

def main():
    N, M = map(int, input().split())
    arr = sorted([int(input()) for _ in range(N)])
    answer = []
    for _ in range(M):
        q = int(input())
        answer.append(index(arr, q))
    print('\n'.join(map(str, answer)))


if __name__ == "__main__":
    main()
