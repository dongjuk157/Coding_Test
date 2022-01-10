import sys
spices, n = {}, 0
while True:
    t = sys.stdin.readline().rstrip()
    if not t: break
    if not spices.get(t):
        spices[t] = 0
    spices[t] += 1
    n += 1

for s in sorted([(k, '{:.4f}'.format(v/n*100)) for k, v in spices.items()]):
    print(*s)
