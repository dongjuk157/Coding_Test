d = [0 for _ in range(10)]
for c in input():
    d[int(c)] += 1
a, t = 0, 0
for i in range(10):
    if i == 6 or i == 9:
        t += d[i]
    else:
        a = max(a, d[i])
print(max(a, (t + 1)//2))