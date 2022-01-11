# import sys; input = sys.stdin.readline

def main():
    N = int(input())
    tropy = [int(input()) for _ in range(N)]
    ans = ''
    max_h, ret = 0, 0
    for i in range(len(tropy)):
        if max_h < tropy[i]:
            max_h = tropy[i]
            ret += 1
    ans += str(ret)+'\n'

    max_h, ret = 0, 0
    for i in range(len(tropy)-1,-1,-1):
        if max_h < tropy[i]:
            max_h = tropy[i]
            ret += 1
    ans += str(ret)
    print(ans)


if __name__ == "__main__":
    main()