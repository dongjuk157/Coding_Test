def main():
    N = int(input())
    s = input()

    f, b = 0, N - 1
    cnt = 0
    while f <= b and f < N and b >= 0:
        init_f = s[f]
        init_b = s[b]
        cnt += 1
        # 순방향 순회
        while f < N and s[f] == init_f:
            f += 1

        if init_f != init_b:
            continue
        # 역방향 순회
        while b >= 0 and s[b] == init_b:
            b -= 1
    print(cnt)

if __name__ == "__main__":
    main()
