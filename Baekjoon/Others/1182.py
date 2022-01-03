def main():
    N, S = map(int, input().split())
    seq = list(map(int, input().split()))

    answer = 0
    for select in range(1, 1 << N):
        tmp = 0
        for i in range(N):
            if select & (1 << i):
                tmp += seq[i]
        if tmp == S:
            answer += 1

    print(answer)

if __name__ == '__main__':
    main()