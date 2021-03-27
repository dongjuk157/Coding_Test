s, t = input(), input()

while len(t)>len(s):
    tmp = t[-1]
    t = t[:-1]
    if tmp == 'B':
        t = t[::-1]
if t == s:
    print(1)
else:
    print(0)