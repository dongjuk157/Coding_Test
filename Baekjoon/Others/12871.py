def gcd(x, y):
    if x > y:
        x, y = y, x
    while x > 0:
        y, x = x, y % x
    return y

def chk(s, t):
    tmp = gcd(len(s), len(t))
    tmp_s = s*(len(t)//tmp)
    tmp_t = t*(len(s)//tmp)
    if tmp_t == tmp_s:
        return 1
    return 0

print(chk(input(), input()))