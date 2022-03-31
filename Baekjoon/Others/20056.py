import sys; input = sys.stdin.readline
d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def main():
    # 0 input
    N, M, K = map(int, input().split())
    fireballs = []
    for _ in range(M):
        ri, ci, mi, si, di = map(int, input().split())
        ri -= 1
        ci -= 1
        fireballs.append([ri, ci, mi, si, di])
    board = [[[] for _ in range(N)] for _ in range(N)]

    # 1 simulation
    for _ in range(K):
        # 1) all fireballs move
        while fireballs:
            ri, ci, mi, si, di = fireballs.pop()
            ri = (ri + d[di][0] * si) % N
            ci = (ci + d[di][1] * si) % N
            board[ri][ci].append([mi, si, di])
        # 2) split fireballs
        for r in range(N):
            for c in range(N):
                if not board[r][c]:
                    continue
                # if len(board[r][c]) >= 1, calculate n
                sum_m, sum_s, sum_num = 0, 0, len(board[r][c])
                tmp_d = []
                while board[r][c]:
                    mi, si, di = board[r][c].pop()
                    sum_m += mi
                    sum_s += si
                    tmp_d.append(di % 2)
                if sum_num > 1:
                    sum_m //= 5
                    sum_s //= sum_num
                    tmp_sum = sum(tmp_d)
                    if tmp_sum == 0 or tmp_sum == sum_num:
                        tmp_d = [0, 2, 4, 6]
                    else:
                        tmp_d = [1, 3, 5, 7]
                else: # sum_num == 1
                    tmp_d = [di]
                # Add fireball in fireballs
                if sum_m:
                    for td in tmp_d:
                        fireballs.append([r, c, sum_m, sum_s, td])
    # 2 output
    answer = sum([m for _, _, m, _, _ in fireballs])
    print(answer)



if __name__ == "__main__":
    main()
