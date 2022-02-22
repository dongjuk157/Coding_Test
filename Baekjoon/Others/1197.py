from heapq import heappop, heappush
def mst(g):
    ret = 0
    visit = [0 for _ in range(len(g))]
    h = [(0, 1)] # cost, start
    while h:
        cur_cost, cur = heappop(h)
        if visit[cur]: continue
        visit[cur] = 1
        ret += cur_cost
        for adj_c, adj in g[cur]:
            heappush(h, (adj_c, adj))
    return ret

def main():
    v, e = map(int, input().split())
    g = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        g[a].append((c, b))
        g[b].append((c, a))

    print(mst(g))


if __name__ == "__main__":
    main()
