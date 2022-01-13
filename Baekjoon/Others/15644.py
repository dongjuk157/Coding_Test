# import sys; input = sys.stdin.readline
from collections import deque
N, M = None, None
_map = None
O = None
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
pd = ['U', 'D', 'L', 'R']

def move(moving, fixed, d):
    nrx, nry = moving
    if _map[moving[0] + d[0]][moving[1] + d[1]] == '#':
        return (False, -1, -1)
    if moving[0] + d[0] == fixed[0] and moving[1] + d[1] == fixed[1]:
        return (False, -1, -1)
    if moving[0] + d[0] == O[0] and moving[1] + d[1] == O[1]:
        return (True, -1, -1)
    return (True, moving[0] + d[0], moving[1] + d[1])


def find_order(r, b, i):
    if i == 0: # up
        return (b, r, False) if r[0] > b[0] else (r, b, True)
    elif i == 1: # down
        return (r, b, True) if r[0] > b[0] else (b, r, False)
    elif i == 2: # left
        return (r, b, True) if r[1] < b[1] else (b, r, False)
    else: # right
        return (b, r, False) if r[1] < b[1] else (r, b, True)


def bfs(r_pos, b_pos):
    q = deque()
    q.append((r_pos, b_pos, ''))
    while q:
        r, b, p = q.popleft()
        # 경로의 길이가 10인데도 안끝났으면 사실 없는거나 마찬가지dlek.
        if len(p) == 10:
            break

        for i in range(len(d)):
            # 탐색하려는 방향이 이전 방향이랑 같으면 넘어간다.
            if p and p[-1] == pd[i]: continue
            # 먼저 움직이는 구슬 구하기
            first, second, first_is_red = find_order(r, b, i)
            # 구슬 이동
            while True:
                possible, *next_first = move(first, second, d[i])
                if not possible:
                    break
                first = next_first
            while True:
                possible, *next_second = move(second, first, d[i])
                if not possible:
                    break
                second = next_second
            # B가 구멍에 빠진 경우 다음 방향 탐색
            if (first_is_red and -1 == second[0] and -1 == second[1]) \
                    or (not first_is_red and -1 == first[0] and -1 == first[1]):
                continue
            # R만 빠진 경우 원하는 값이므로 경로 리턴
            elif (first_is_red and -1 == first[0] and -1 == first[1]) \
                    or (not first_is_red and -1 == second[0] and -1 == second[1]):
                return f'{len(p)+1}\n{p + pd[i]}'

            # 움직임이 없으면 추가하지 않음
            if first_is_red:
                if first[0] == r[0] and first[1] == r[1] and second[0] == b[0] and second[1] == b[1]:
                    continue
            else:
                if second[0] == r[0] and second[1] == r[1] and first[0] == b[0] and first[1] == b[1]:
                    continue
            # queue에 값 추가
            if first_is_red:
                q.append((first, second, p + pd[i]))
            else:
                q.append((second, first, p + pd[i]))
    # 탐색해도 경로를 못찾은 경우 -1 리턴
    return -1

def main():
    global N, M, _map, O
    # 0 입력
    N, M = map(int, input().split())
    _map = []
    r, b = None, None
    for i in range(N):
        tmp = input()
        _map.append(tmp.rstrip())
        for j in range(M):
            if tmp[j] == 'R':
                r = (i, j)
            elif tmp[j] == 'B':
                b = (i, j)
            elif tmp[j] == 'O':
                O = (i, j)
    # 1 탐색
    answer = bfs(r, b)
    # 2 출력
    print(answer)

if __name__ == "__main__":
    main()
