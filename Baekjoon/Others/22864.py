a, b, c, m = map(int, input().split())
p, an, h = 0, 0, 24
while h:
    if p + a <= m:
        p += a
        an += b
    else:
        p -= c
        if p < 0:
            p = 0
    h -= 1
print(an)
