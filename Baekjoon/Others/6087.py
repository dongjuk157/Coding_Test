import sys; input = sys.stdin.readline
from heapq import heappop, heappush

def dijkstra(raser, _map):
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ret = 10000
    # s = raser[0], e = raser[1]
    visit = [[[-1, 10000] for _ in range(len(_map[0]))] for _ in range(len(_map))]
    h = [(0, raser[0][0], raser[0][1], -1, 0)]
    while h:
        dist, cur_r, cur_c, cur_dir, change_num = heappop(h)
        if cur_r == raser[1][0] and cur_c == raser[1][1]:
            # 방향이 바뀌는 최소 횟수 저장
            ret = min(ret, change_num)
        if visit[cur_r][cur_c][1] >= change_num:
            visit[cur_r][cur_c][1] = change_num
        elif visit[cur_r][cur_c][0] > -1:
            continue
        visit[cur_r][cur_c][0] = dist

        for i in range(4):
            nr = cur_r + d[i][0]
            nc = cur_c + d[i][1]
            n_num = change_num
            if _map[nr][nc] == "*": continue
            if cur_dir != -1 and cur_dir != i:
                n_num += 1
            heappush(h, (dist + 1, nr, nc, i, n_num))

    return ret


def main():
    W, H = map(int, input().split())
    raser = []
    _map = ["*" * (W + 2)]
    for r in range(H):
        tmp = input().rstrip()
        _map.append("*" + tmp + "*")
        for c in range(W):
            if tmp[c] == "C":
                raser.append((r + 1, c + 1))
    _map.append("*" * (W + 2))

    print(dijkstra(raser, _map))


if __name__ == "__main__":
    main()

