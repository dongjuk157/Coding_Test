# import sys; input = sys.stdin.readline

def check():
    global N, L, _map
    ret = 0

    for r in range(N):
        h = _map[r][0]
        cnt = 1
        for c in range(1, N):
            if h == _map[r][c]:
                cnt += 1
                h = _map[r][c]
                continue
            if h == _map[r][c] - 1 and cnt >= L:
                h = _map[r][c]
                cnt = 1
                continue
            elif h == _map[r][c] + 1:
                for i in range(1, L):
                    if c + i < N and _map[r][c + i] == _map[r][c]:
                        continue
                    break
                else:
                    h = _map[r][c]
                    cnt = -L + 1
                    continue
            break
        else:
            ret += 1

    for c in range(N):
        h = _map[0][c]
        cnt = 1
        for r in range(1, N):
            if h == _map[r][c]:
                cnt += 1
                h = _map[r][c]
                continue
            if h == _map[r][c] - 1 and cnt >= L:
                h = _map[r][c]
                cnt = 1
                continue
            elif h == _map[r][c] + 1:
                for i in range(1, L):
                    if r + i < N and _map[r + i][c] == _map[r][c]:
                        continue
                    break
                else:
                    h = _map[r][c]
                    cnt = -L + 1
                    continue
            break
        else:
            ret += 1

    return ret

def main():
    global N, L, _map
    N, L = map(int, input().split())
    _map = [list(map(int, input().split())) for _ in range(N)]
    answer = check()
    print(answer)


if __name__ == "__main__":
    main()
