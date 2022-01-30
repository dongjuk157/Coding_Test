import sys; input = sys.stdin.readline
from itertools import accumulate

def main():
    R, C, Q = map(int, input().split())
    memo = [[0 for _ in range(C + 1)]]
    for i in range(1, R + 1):
        lst = [0]
        lst.extend(map(int, input().split()))
        memo.append(list(accumulate(lst)))

    for i in range(1, R + 1):
        for j in range(1, C + 1):
            memo[i][j] += memo[i - 1][j]

    ans = []
    for _ in range(Q):
        r1, c1, r2, c2 = map(int, input().split())
        area = memo[r2][c2] - memo[r1 - 1][c2] - memo[r2][c1 - 1] + memo[r1 - 1][c1 - 1]
        num_of_area = (r2 - r1 + 1) * (c2 - c1 + 1)
        ans.append(area // num_of_area)
    print('\n'.join(map(str, ans)))


if __name__ == "__main__":
    main()
