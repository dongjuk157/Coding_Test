from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
que=deque()
cmd_list=[]
for i in range(n):
    cmd_list.append(input().split())

for cmd in cmd_list:
    if cmd[0] == 'pop':
        try:
            print(que.popleft())
        except:
            print(-1)
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        print(0 if len(que) else 1)
    elif cmd[0] == 'front':
        try:
            print(que[0])
        except:
            print(-1)
    elif cmd[0] =='back':
        try:
            print(que[-1])
        except:
            print(-1)
    elif cmd[0]=='push':
        que.append(int(cmd.pop()))


