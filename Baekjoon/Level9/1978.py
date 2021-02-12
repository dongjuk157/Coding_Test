# 4
# 1 3 5 7

n = int(input())
number = list(map(int, input().split()))
result = 0
for num in number:
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        result += 1
print(result)