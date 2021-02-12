# 1 + 6 + 12 + 18 +
# 1   7   19   37 ...

n=int(input())
cnt = 0
result = 1
while True:
    cnt += 1
    result += 6*(cnt-1)
    if n <= result:
        print(cnt)
        break


    
    