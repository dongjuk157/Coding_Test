import sys
sys.stdin = open("./.idea/inputs/2615_input.txt", "r")

badukpan = list()
max_width = 19
plus_width = 5
for _ in range(plus_width):
    tmp = [0]*(max_width+2*plus_width)
    badukpan.append(tmp)

for _ in range(max_width):
    tmp=[0] * plus_width
    tmp.extend(list(map(int, input().split())))
    tmp.extend([0]*plus_width)
    badukpan.append(tmp)

for _ in range(plus_width):
    tmp = [0]*(max_width+2*plus_width)
    badukpan.append(tmp)

# for baduk in badukpan:
#     print(baduk)
result = 0
for i in range(plus_width,plus_width+max_width):
    for j in range(plus_width,plus_width+max_width):
        tmp = badukpan[i][j]
        # 방향마다 총 6개씩 확인, 총 네 방향 확인

        if tmp: # tmp가 0인 아닌경우에만 확인
            # 1 우향
            if tmp != badukpan[i][j - 1]:
                for k in range(1,5):
                    if tmp != badukpan[i][j+k]:
                        break
                else:
                    if tmp != badukpan[i][j+5]:
                        result = (tmp, i, j)

            #2 우하향
            if tmp != badukpan[i - 1][j - 1]:
                for k in range(1,5):
                    if tmp != badukpan[i+k][j+k]:
                        break
                else:
                    if tmp != badukpan[i+5][j+5]:
                        result = (tmp, i,j)

            #3 하향
            if tmp != badukpan[i - 1][j]:
                for k in range(1,5):
                    if tmp != badukpan[i+k][j]:
                        break
                else:
                    if tmp != badukpan[i+5][j]:
                        result = (tmp, i, j)

            #4 좌하향
            if tmp != badukpan[i - 1][j + 1]:
                for k in range(1,5):
                    if tmp != badukpan[i+k][j-k]:
                        break
                else:
                    if tmp != badukpan[i+5][j-5]: #0,5 => 4,1
                        result = (tmp, i+4,j-4)

if result != 0:
    print("{}\n{} {}".format(result[0],result[1]-plus_width+1,result[2]- plus_width+1))
else:
    print(0)
