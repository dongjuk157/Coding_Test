'''
boj 22942
wrong answer
'''
# import sys; input = sys.stdin.readline
from itertools import combinations

def check(circles):
    for (x, r), (xx, rr) in combinations(circles, 2):
        # 동심원인데 반지름까지 같은 경우
        if x == xx and r == rr:
            return False

        # 한 점에서 만나는 경우
        d = abs(x - xx) # 중심 사이 거리
        if r + rr == d or abs(r - rr) == d:
            return False

        # 두 점에서 만나는 경우
        if abs(r - rr) < d < r + rr:
            return False

    return True

def main():
    N = int(input())
    circles = [tuple(map(int, input().split())) for _ in range(N)]

    if check(circles):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
