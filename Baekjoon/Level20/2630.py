import sys; input = sys.stdin.readline
N = int(input())
color_paper = [list(map(int, input().split())) for _ in range(N)]
def check(color, r, c, size):
    for i in range(r, r + size, visit[r][c]):
        for j in range(c, c + size, visit[r][c]):
            if color_paper[i][j] != color:
                return False
            if visit[r][c] != visit[i][j]:
                return False
    visit[r][c] *= 2
    return True

# bottom up
white, blue = 0, 0
for r in color_paper:
    tmp = sum(r)
    blue += tmp
    white += N - tmp

cnt = 2
visit = [[1] * N for _ in range(N)] # 어떤 크기로 합쳐져있는지 확인하기 위한 값
while cnt <= N:
    # cnt 등분 되어있는 모든 색종이를 확인
    for i in range(0, N, cnt):
        for j in range(0, N, cnt):
            ret = check(color_paper[i][j], i, j, cnt)
            if ret: # 합칠수 있음, 작은색종이 4-> 큰색종이 1
                if color_paper[i][j]: # 파란색 
                    blue -= 3 
                else:
                    white -= 3
    # 한바퀴 다 돌면 cnt *= 2
    cnt <<= 1
print(white, blue, sep='\n')
