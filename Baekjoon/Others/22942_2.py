# import sys; input = sys.stdin.readline
from bisect import insort, bisect

def check(circles, start=None, end=None):
    if start is None: start = 0
    if end is None: end = len(circles)

    s = []
    for i in range(start, end):
        c = circles[i]
        if not s:
            s.append(c)
            continue
        ppos, pbra, pnum = s[-1]
        pos, bra, num = c
        if ppos == pos:
            return False
        if pnum == num:
            s.pop()
            continue

        if not bra:
            s.append(c)
        else:  # if bra == ']':
            return False

    return True


def main():
    N = int(input())
    circles = []
    answer = "YES"
    for i in range(N):
        x, r = map(int, input().split())
        circles.append((x - r, False, i))
        circles.append((x + r, True, i))
    circles.sort()

    if not check(circles):
        answer = "NO"
    print(answer)


if __name__ == "__main__":
    main()
