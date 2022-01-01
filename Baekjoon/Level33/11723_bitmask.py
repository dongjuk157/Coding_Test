import sys;input = sys.stdin.readline
S = 0
answer = ''
for _ in range(int(input())):
    command = input()
    if command[0] == 'a' and command[1] == 'd':
        num = int(command.split()[1])
        S |= (1 << (num - 1))
    elif command[0] == 'a' and command[1] == 'l':  # all
        S = (2 ** 21) - 1
    elif command[0] == 'r':
        num = int(command.split()[1])
        S &= ~(1 << (num - 1))
    elif command[0] == 'c':
        num = int(command.split()[1])
        if (S >> (num - 1)) & 1:
            answer += '1\n'
        else:
            answer += '0\n'
    elif command[0] == 't':
        num = int(command.split()[1])
        if (S >> (num - 1)) & 1:
            S &= ~(1 << (num - 1))
        else:
            S |= (1 << (num - 1))
    else:  # command[0] == 'e':
        S = 0
print(answer)