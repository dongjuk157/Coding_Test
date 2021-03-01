# 1. 배열의 크기만큼 반복문 중첩
arr = [1, 2, 3]
subset = list()
for k in range(2):
    for j in range(2):
        for i in range(2):
            tmp = []
            if arr[0]*i:
                tmp.append(arr[0] * i)
            if arr[1]*j:
                tmp.append(arr[1] * j)
            if arr[2]*k:
                tmp.append(arr[2] * k)
            subset.append(tmp)
print(subset)

# 2. 비트연산자 사용
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)
subset = list()
for i in range(1 << n):
    tmp = []
    for j in range(n+1):
        if i & (1 << j):
            tmp.append(arr[j])
    subset.append(tmp)
print(subset)

