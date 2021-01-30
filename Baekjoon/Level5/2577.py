a = int(input())
b = int(input())
c = int(input())
str_num = str(a*b*c)

result = dict()     # dictionary 초기화
for i in range(10):
    result[f'{i}'] = 0

for num in str_num:
    result[num] += 1

for val in result.values():
    print(val)