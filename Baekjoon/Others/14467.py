# import sys; input = sys.stdin.readline
def main():
    N = int(input())
    cow = [None for _ in range(11)]
    answer = 0
    for _ in range(N):
        a, b = map(int, input().split())
        if cow[a] is None:
            cow[a] = b
        elif cow[a] != b:
            answer += 1
            cow[a] = b
    print(answer)



if __name__ == "__main__":
    main()
