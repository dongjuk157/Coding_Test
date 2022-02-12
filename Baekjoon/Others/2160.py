# import sys; input = sys.stdin.readline
from itertools import combinations


def check_diff(i, j, pictures):
    ret = 0
    for r in range(5):
        for c in range(7):
            if pictures[i][r][c] != pictures[j][r][c]:
                ret += 1
    return ret


def main():
    N = int(input())
    pictures = [[input().rstrip() for _ in range(5)] for _ in range(N)]
    diff = 36
    answer = [0, 0]
    for i, j in combinations(range(N), 2):
        tmp_diff = check_diff(i, j, pictures)
        if diff > tmp_diff:
            diff = tmp_diff
            answer[0], answer[1] = i + 1, j + 1
    print(*answer)


if __name__ == "__main__":
    main()
