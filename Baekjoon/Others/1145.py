num = list(map(int,input().split()))
num.sort()
result = num[2]*num[3]*num[4]
for i in range(num[0],result):

    cnt = 0
    if i % num[0] == 0:
        cnt += 1
    if i % num[1] == 0:
        cnt += 1
    if i % num[2] == 0:
        cnt += 1
    if i % num[3] == 0:
        cnt += 1
    if i % num[4] == 0:
        cnt += 1
    if cnt >= 3:
        result = i
        break
print(result)