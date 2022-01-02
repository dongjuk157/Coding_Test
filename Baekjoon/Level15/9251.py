a, b = input(), input()
c, r = len(a), len(b)
t = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
for rr in range(r):
    for cc in range(c):
        if a[cc] == b[rr]:
            t[rr+1][cc+1] = max(t[rr + 1][cc], t[rr][cc + 1], t[rr][cc] + 1)
        else:
            t[rr+1][cc+1] = max(t[rr+1][cc], t[rr][cc+1])

print(t[r][c])
