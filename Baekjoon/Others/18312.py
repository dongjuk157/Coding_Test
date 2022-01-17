def main():
    N, K = map(int, input().split())
    cnt = 0
    for i in range(N + 1):
        for j in range(60):
            for k in range(60):
                if str(K) in str(i).zfill(2) or \
                        str(K) in str(j).zfill(2) or \
                        str(K) in str(k).zfill(2):
                    cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()