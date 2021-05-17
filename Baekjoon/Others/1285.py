# https://nicotina04.tistory.com/33
import sys; input = sys.stdin.readline
n = int(input())
coin = [[False] * n for _ in range(n)]
cnt = 401 # 최대값이 20*20 /2 인데 그냥 계산하기 편하게 400 + 1
# head: 0, tail: 1
for i in range(n):
    tmp = input()
    for j in range(n):
        if tmp[j] == 'T':
            coin[i][j] = True

# bit = (1 << n) - 1
for bit in range(1 << n):
    new_coin = [[False] * n for _ in range(n)]
    # deep copy
    for i in range(n):
        for j in range(n):
            new_coin[i][j] = coin[i][j]
    # 행을 뒤집는 경우를 완전 탐색(근데 bit를 곁들인)
    for i in range(n):
        if bit & (1 << i):
            for j in range(n):
                new_coin[i][j] = not new_coin[i][j]
    # 각 열에 대해 뒤집는경우와 뒤집지 않는 경우를 판단하여, T가 적은쪽으로 열을 뒤집음
    cmpcnt = 0
    for i in range(n):
        f, b = 0, 0
        for j in range(n):
            if new_coin[j][i]:
                f += 1
            else:
                b += 1
        cmpcnt += (b if f > b else f)
    if cnt > cmpcnt :
        cnt = cmpcnt
    # bit -= 1
print(cnt)
