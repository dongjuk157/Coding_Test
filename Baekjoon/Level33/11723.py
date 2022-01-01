import sys;input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    command = input()
    if command[0] == 'a':
        if command[1] == 'd':
            S.add(int(command.split()[1]))
        else: # all
            S = set(range(1, 21))
    elif command[0] == 'r':
        num = int(command.split()[1])
        if num in S:
            S.remove(num)
    elif command[0] == 'c':
        print(1 if int(command.split()[1]) in S else 0)
    elif command[0] == 't':
        num = int(command.split()[1])
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    else:# command[0] == 'e':
        S = set()



