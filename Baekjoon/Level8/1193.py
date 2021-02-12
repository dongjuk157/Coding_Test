x=int(input())

dp = [0,1]
result = 1
cnt = 1
while dp[-1]<x:
    cnt += 1
    result += cnt
    dp.append(result)
#분자/분모  -> cnt가 홀짝에 따라 달라짐
if cnt%2: #odd
    ja=cnt+1-x+dp[-2]
    mo=x-dp[-2]
else:   #even
    ja=x-dp[-2]
    mo=cnt+1-x+dp[-2]
print(f'{ja}/{mo}')