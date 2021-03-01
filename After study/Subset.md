# 부분집합

집합의 원소가 n개 인경우 공집합을 포합한 부분집합의 수는 2^n개

- `{1,2,3}` 인 경우 `{},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}` 총 8 개



부분집합을 만드는(구하는) 방법

```python
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
```

```python
# 2. 비트연산자 사용
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)
subset = list()
for i in range(1<<n): 		# 1 ~ (2**6 - 1) => 0b00000 ~ 0b11111
    tmp = []
    for j in range(n+1):	# 1 ~ (6-1)
        if i & (1<<j): 		# if i = 7(0b00111), j=2=> 1<<2 = 4 = 0b00100 => True
            				# if i = 7(0b00111), j=3=> 1<<3 = 8 = 0b01000 => False
            tmp.append(arr[j])	# arr[2] = 7, arr[3] = 1
    subset.append(tmp)
print(subset)
```

```python
# 3. 백트래킹

```



