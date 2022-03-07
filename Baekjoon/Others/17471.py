# import sys; input = sys.stdin.readline
from collections import deque

def check(limit):
    global population, graph, answer, visit
    ret = [0, 0, 0] # T/F, area1, area2
    # 선거구가 한쪽에 몰려있는 경우
    if 0 == sum(visit) or limit == sum(visit):
        return ret

    # 선거구끼리 연결이 되어있지 않은 경우 탐색
    area1 = set()
    area2 = set()
    for i, v in enumerate(visit):
        if i == 0: continue
        if v:
            area1.add(i)
            ret[1] += population[i]
        else:
            area2.add(i)
            ret[2] += population[i]
    visit_area1 = [0 for _ in range(len(visit))]
    visit_area2 = [0 for _ in range(len(visit))]
    q = deque()
    for e in area1:
        q.append(e)
        break
    while q:
        cur = q.popleft()
        if visit_area1[cur]: continue
        visit_area1[cur] = 1
        for adj in graph[cur]:
            if adj in area1:
                q.append(adj)
    if sum(visit_area1) != len(area1):
        return ret

    for e in area2:
        q.append(e)
        break
    while q:
        cur = q.popleft()
        if visit_area2[cur]: continue
        visit_area2[cur] = 1
        for adj in graph[cur]:
            if adj in area2:
                q.append(adj)
    if sum(visit_area2) != len(area2):
        return ret

    # 선거구가 모두 연결되어있는 경우
    ret[0] = 1
    return ret

def backtrack(ind, limit):
    global population, graph, answer, visit
    if ind == limit:
        # 선거구끼리 모두 연결되어있는지 확인
        tmp = check(limit)
        if tmp[0]:
            # 연결되어있으면 최솟값 갱신
            answer = min(answer, abs(tmp[1] - tmp[2]))
        return
    # 탐색
    visit[ind + 1] = 1
    backtrack(ind + 1, limit)
    visit[ind + 1] = 0
    backtrack(ind + 1, limit)


def main():
    global population, graph, answer, visit
    # 0 input
    N = int(input())
    population = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for idx, v in enumerate(map(int, input().split())):
            if idx:
                graph[i].append(v)
    # 1 find combinations
    visit = [0 for _ in range(N + 1)]
    answer = N * 100
    backtrack(0, N)
    if answer == N * 100:
        answer = -1
    # 2 output
    print(answer)


if __name__ == "__main__":
    main()
