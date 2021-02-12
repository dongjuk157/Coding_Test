n=int(input())
result = 0
break_chk = False
while n>0:
    if n % 5 == 0:
        result += n // 5
        break_chk = True
        break
    else:
        n -= 3
        result += 1
        if n==0:
            break_chk = True

if break_chk:
    print(result)
else:
    print(-1)