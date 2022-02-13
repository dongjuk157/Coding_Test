from heapq import heappop, heappush
def solution(n, costs):
    answer = 0
    adj_list = [[] for _ in range(n)]
    for s, e, c in costs:
        adj_list[s].append((c, e))
        adj_list[e].append((c, s))
    # prim
    visit = [0 for _ in range(n)]
    h = [(0, 0)]
    while h:
        cur_d, cur = heappop(h)
        if visit[cur]:
            continue
        visit[cur] = 1
        answer += cur_d
        for adj_d, adj in adj_list[cur]:
            heappush(h, (adj_d, adj))
        
    return answer