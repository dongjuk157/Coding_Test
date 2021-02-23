import sys
#input = sys.stdin.readline
sys.stdin = open(".idea/inputs/2628_input1.txt")

width, height = map(int, input().split())
width_cut=[0]
height_cut=[0]
n = int(input())
for _ in range(n):
    direction, nth = map(int, input().split())
    if direction: # 세로
        width_cut.append(nth)
    else:   #가로
        height_cut.append(nth)
width_cut.append(width)
width_cut.sort()
height_cut.append(height)
height_cut.sort()

max_width, max_height = 0, 0
for i in range(len(width_cut)-1):
    tmp = width_cut[i+1] - width_cut[i]
    if max_width < tmp:
        max_width = tmp

for i in range(len(height_cut)-1):
    tmp = height_cut[i+1] - height_cut[i]
    if max_height < tmp:
        max_height = tmp

print(max_width * max_height)
