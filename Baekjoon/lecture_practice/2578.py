import sys

def isbingo(_list):
    result = 0
    #1 가로 확인
    for i in range(5):
        for j in range(5):
            if not _list[i][j]:
                break
        else:
            result += 1

    #2 세로 확인
    for j in range(5):
        for i in range(5):
            if not _list[i][j]:
                break
        else:
            result += 1

    #3 대각선 확인
    for k in range(5): # 00,11,22,33,44
        if not _list[k][k]:
            break
    else:
        result += 1

    for k in range(5): #04,13,22,31,40
        if not _list[k][4-k]:
            break
    else:
        result += 1

    return result

#input = sys.stdin.readline
sys.stdin = open(".idea/inputs/2578_input1.txt")
my_bingo = []
bingo_seq = []
my_bingo_bool = [[False]*5 for i in range(5)]

for _ in range(5):
    my_bingo.append(list(map(int,input().split())))
for _ in range(5):
    bingo_seq.extend(list(map(int,input().split())))
cnt = 0
for seq in bingo_seq:
    cnt += 1
    break_chk = False
    for i in range(5):
        for j in range(5):
            if my_bingo[i][j] == seq:
                my_bingo_bool[i][j] = True
                break_chk = True
                break
        if break_chk:
            break

    if isbingo(my_bingo_bool)>2:
        break
print(cnt)