a, b = map(int, input().split())
result = 1
break_chk = False
while b > a:
    result += 1
    if b & 1 == 0:
        b = b >> 1
    elif b % 10 == 1:
        b //= 10
    else:
        break_chk = True
        break
else:
    if a == b:
        print(result)
    else:
        print(-1)

if break_chk:
    print(-1)