import sys; input = sys.stdin.readline
from collections import deque
T = int(input())
for tc in range(T):
    p = input().rstrip()
    n = int(input())
    x_arr = input().rstrip()
    if x_arr == '[]':
        x_arr = deque()
    else:
        x_arr = deque(map(int, x_arr[1:-1].split(',')))

    index = 0
    dir = True # True 정방향
    while index < len(p):
        ch = p[index]
        if ch == 'R':
            dir = not dir
        elif x_arr: # ch == 'D'
            if dir:
                x_arr.popleft()
            else:
                x_arr.pop()
        else: # not x_arr and ch == 'D'
            print("error")
            break
        index += 1
    else:
        if x_arr:
            if dir:
                print('[{}]'.format(','.join(map(str, x_arr))))
            else:
                print('[{}]'.format(','.join(map(str, reversed(x_arr)))))
        else:
            print('[]')
