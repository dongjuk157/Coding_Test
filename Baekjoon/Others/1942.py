time_dict = dict()
prev = None
for i in range(24):
    time_dict[i * 10000 - 1] = time_dict[prev] if prev is not None else 0
    for j in range(60):
        time_dict[i * 10000 + j * 100 - 1] = time_dict[prev] if prev is not None else 0
        for k in range(60):
            tmp = i * 10000 + j * 100 + k
            time_dict[tmp] = time_dict[prev] if prev is not None else 0
            if not tmp % 3:
                time_dict[tmp] += 1
            prev = tmp

ans = ''
for _ in range(3):
    num1, num2 = map(lambda x:(int(''.join(x.split(":")))), input().split())
    tmp = 0
    if num1 > num2:
        tmp = time_dict[235959] - time_dict[num1 - 1] + time_dict[num2] - time_dict[-1]
    else:
        tmp = time_dict[num2] - time_dict[num1 - 1]
    ans += f'{tmp}\n'
print(ans)
