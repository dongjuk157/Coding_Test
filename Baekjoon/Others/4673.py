def d(n):
    result = n
    while n > 0:
        result += n % 10
        n = n // 10
    return result

self_num = [False]+[True]*10000
for number in range(1,10001):
    tmp = d(number)
    if tmp<=10000:  # 생성자가 하나라도 있으면 False
        self_num[tmp] = False

for number, isselfnum in enumerate(self_num):
    if isselfnum:
        print(number)
    