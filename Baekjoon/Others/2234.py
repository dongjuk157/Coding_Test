# import sys; input = sys.stdin.readline
from collections import deque

d = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # west/north/east/south
def bfs(sr, sc):
    global N, M, castle, visit, num_room, adj_list
    q = deque()
    q.append((sr, sc))
    size = 0
    adj_list.append(set())
    while q:
        r, c = q.popleft()
        if visit[r][c]: continue
        size += 1
        visit[r][c] = num_room
        for i in range(4):
            nr, nc = r + d[i][0], c + d[i][1]
            if 0 > nr or nr >= M or 0 > nc or nc >= N:
                continue
            if castle[r][c] & (1 << i):
                # if bit value is 1, there is a wall
                if visit[nr][nc] and visit[nr][nc] != num_room:
                    # make graph
                    adj_list[num_room].add(visit[nr][nc])
                    adj_list[visit[nr][nc]].add(num_room)
                continue
            q.append((nr, nc))
        
    return size


def main():
    global N, M, castle, visit, num_room, adj_list
    N, M = map(int, input().split())
    castle = [list(map(int, input().split())) for _ in range(M)]
    visit = [[0 for _ in range(N)] for _ in range(M)]
    num_room = 0
    room_size = [0]
    adj_list = [set()]
    # find maximum size, and a number of rooms
    for i in range(M):
        for j in range(N):
            if visit[i][j]: continue
            num_room += 1
            room_size.append(bfs(i, j))
    max_size = max(room_size)

    # find maximum size about combining two rooms
    max_c_size = 0
    select = [0 for _ in range(num_room + 1)]
    for i in range(1, num_room + 1):
        select[i] = 1
        for adj in adj_list[i]:
            if select[adj]: continue
            max_c_size = max(max_c_size, room_size[i]+room_size[adj])

    # output
    print(num_room, max_size, max_c_size, sep='\n')

if __name__ == "__main__":
    main()