m = int(input())
n = int(input())
result = []
for i in range(m, n+1):
    if i == 1:  ## 1인 경우도 생각해봐야한다.
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        result.append(i)
if result == []:
    print(-1)
else:
    print(sum(result))
    print(result[0])

