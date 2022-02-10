# import sys; input = sys.stdin.readline

def main():
    N = int(input())
    num_task = [0 for _ in range(366)]
    for _ in range(N):
        s, e = map(int, input().split())
        for i in range(s, e + 1):
            num_task[i] += 1

    total = 0
    h, w = 0, 0
    for i in range(1, 366):
        if num_task[i]:
            h = max(h, num_task[i])
            w += 1
        else: # num_task[i] == 0
            total += h * w
            h, w = 0, 0

    total += h * w
    print(total)


if __name__ == "__main__":
    main()
