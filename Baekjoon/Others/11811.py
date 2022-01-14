import sys; input = sys.stdin.readline

def main():
    N = int(input())
    ans = [0 for _ in range(N)]
    for i in range(N):
        for nij in map(int, input().split()):
            ans[i] |= nij
    print(*ans)


if __name__ == "__main__":
    main()