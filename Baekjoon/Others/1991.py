import sys; input = sys.stdin.readline
n = int(input())
ldic, rdic = dict(), dict()
for _ in range(n):
    p, ls, rs = input().split()
    ldic[p] = ls
    rdic[p] = rs

def pre(node='A'):
    global answer
    if node == '.':
        return
    answer += node
    pre(ldic[node])
    pre(rdic[node])

def ino(node='A'):
    global answer
    if node == '.':
        return
    ino(ldic[node])
    answer += node
    ino(rdic[node])

def pos(node='A'):
    global answer
    if node == '.':
        return
    pos(ldic[node])
    pos(rdic[node])
    answer += node
answer = ''
pre()
answer += '\n'
ino()
answer += '\n'
pos()
print(answer)
