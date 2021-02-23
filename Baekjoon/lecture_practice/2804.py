import sys
input = sys.stdin.readline

a, b = input().split()
n, m = len(a), len(b)
r, c = 0, 0
break_chk = False
for ind_a in range(n):
    for ind_b in range(m):
        if a[ind_a] == b[ind_b]:
            r = ind_b
            c = ind_a
            break_chk = True
            break
    if break_chk:
        break
matrix = []
cnt = 0
for row in range(m):
    if row == r:
        matrix.append(a)
    else:
        matrix.append('.' * c + b[cnt] + '.' * (n - c - 1))
    cnt += 1
for m in matrix:
    print(m)