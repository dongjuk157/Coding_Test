n=int(input())
num = [int(input()) for _ in range(n)]

result = 0
for i in range(n-2,-1,-1):
    if num[i] >= num[i+1]:
        result += num[i] - num[i+1] + 1
        num[i] = num[i+1] - 1
print(result)

