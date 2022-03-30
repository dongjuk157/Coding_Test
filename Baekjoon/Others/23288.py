import sys; input = sys.stdin.readline
from collections import deque
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # r d l u, clockwise

def move():
    global N, M, direction, pos
    if 0 > direction or direction > 3:
        return
    r, c = pos
    nr, nc = r + d[direction][0], c + d[direction][1]
    if 0 >= nr or nr > N or 0 >= nc or nc > M:
        direction = (direction + 2) % 4
        nr, nc = r + d[direction][0], c + d[direction][1]

    pos[0], pos[1] = nr, nc
    return

def change_dice():
    global direction, dice
    if 0 > direction or direction > 3:
        return
    if 0 == direction:
        # rolling east
        dice[1], dice[3], dice[4], dice[6] = \
            dice[4], dice[1], dice[6], dice[3]
    elif 1 == direction:
        # rolling south
        dice[1], dice[2], dice[5], dice[6] = \
            dice[2], dice[6], dice[1], dice[5]
    elif 2 == direction:
        # rolling west
        dice[1], dice[3], dice[4], dice[6] = \
            dice[3], dice[6], dice[1], dice[4]
    elif 3 == direction:
        # rolling north
        dice[1], dice[2], dice[5], dice[6] = \
            dice[5], dice[1], dice[6], dice[2]
    return

def get_score():
    # graph traversal(BFS)
    global N, M, _map, pos
    score = 0
    visit = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
    q = deque()
    q.append(pos)
    while q:
        r, c = q.popleft()
        if visit[r][c]: continue
        visit[r][c] = 1
        score += _map[pos[0]][pos[1]]
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 < nr <= N and 0 < nc <= M:
                if _map[nr][nc] == _map[pos[0]][pos[1]]:
                    q.append((nr, nc))

    return score


def get_next_direction(A, B):
    global direction
    if A > B:
        direction += 1
    elif A < B:
        direction -= 1
    else:
        # no change
        pass
    direction %= 4
    return

def main():
    global N, M, _map, direction, pos, dice
    # 0 input
    N, M, K = map(int, input().split())
    _map = [[0 for _ in range(M + 2)]]      # make boundary
    for _ in range(N):
        tmp = [0]                           # make boundary
        tmp.extend(map(int, input().split()))  # real value
        tmp.append(0)                       # make boundary
        _map.append(tmp)
    _map.append([0 for _ in range(M + 2)])  # make boundary
    dice = list(range(7))                   # init dice array

    # 1 simulation
    answer = 0
    pos = [1, 1]    # initial position
    direction = 0   # initial direction is right
    for _ in range(K):
        move()
        change_dice()
        answer += get_score()
        get_next_direction(dice[6], _map[pos[0]][pos[1]])

    # 2 output
    print(answer)


if __name__ == "__main__":
    main()
