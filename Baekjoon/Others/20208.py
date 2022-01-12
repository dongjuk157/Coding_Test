import sys; input = sys.stdin.readline
answer = 0
H = 0
visit = None
mint_choco = None
start = None

def distance(a, b):
    return abs(a[0]- b[0]) + abs(a[1] - b[1])

def dfs(ind, M, last, total):

    #현재 값이 최고인지 확인
    global answer
    if ind != 0:
        if distance(last, start) <= M:
            answer = max(answer, total)
    if ind == len(mint_choco):
        return

    for i in range(len(mint_choco)):
        if visit[i]: continue
        tmp_dist = distance(last, mint_choco[i])
        if M < tmp_dist: continue
        visit[i] = True
        dfs(ind + 1, M + H - tmp_dist, mint_choco[i], total + 1)
        visit[i] = False


def main():
    global visit, mint_choco, start, H
    N, M, H = map(int, input().split())
    mint_choco = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(N):
            if tmp[j] == 1:
                start = (i, j)
            elif tmp[j] == 2:
                mint_choco.append((i, j))
    visit = [False for _ in range(len(mint_choco))]
    # dfs(ind, M, last, total)
    dfs(0, M, start, 0)

    print(answer)


if __name__ == '__main__':
    main()