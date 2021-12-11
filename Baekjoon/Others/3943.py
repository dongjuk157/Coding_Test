import sys
input = sys.stdin.readline
t = int(input())
answer = ''
for _ in range(t):
    n = int(input())
    max_num = n
    while n != 1:
        if n & 1: #odd
            n = 3 * n + 1
            if max_num < n:
                max_num = n
        else:
            n = n >> 1
    answer += "{}\n".format(max_num)
print(answer)