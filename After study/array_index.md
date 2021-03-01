# 배열의 접근

### 일차원 배열

기본적인 배열(리스트) 

접근: `arr[index]`

```python
arr = [1,2,3,4,5,6,7]
# 순방향 접근
for i in range(len(arr)):
    print(arr[i], end=' ')
print()
# 역방향 접근
for j in range(len(arr)-1, -1, -1):
    print(arr[j], end=' ')
```



### 이차원 배열

- 1차원 리스트를 묶어놓은 리스트
- arr\[i]\[j]

접근

- 행 우선 순회

  ```python
  for i in range(len(array)):
      for j in range(len(array[i])):
          array[i][j]
  ```

- 열 우선 순회

  ```python
  for j in range(len(array[0])):
      for i in range(len(array)):
          array[i][j]
  ```

- 지그재그 순회

  ```python
  for i in range(len(array)):
      for j in range(len(array[0])):
          array[i][j + (m-1-2*j)*(i % 2)] # n*m의 배열이므로 m=len(array[0])
          # 2*3 행렬 [[1,2,3],[4,5,6]]
          # 0행 [i][j]
          # 1행 [i][m-1-*j]
  ```

- 델타를 이용한 2차 배열 탐색

  ```python
  #array: n*n
  dx= [0, 0, -1, 1]
  dy= [-1, 1, 0, 0]
  for x in range(len(array)):
      for y in range(len(array[x])):
          for i in range(4):
              textX = x + dx[i]
              testY = y + dy[i]
              test(array[testX][testY])
  ```

  - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

  - 이렇게만 사용하면 index 에러가 날수도있고, 원하지 않는 값을 가져올수도 있다.

    - 조건문을 줘야함 `if 0<=nr<=n or 0<=nc<=n: pass`

  - 대각선은 어떻게 확인?

    - 비슷한 방법으로 주면됨. 

    - ```python
      #시계방향으로 8방향, 상, 우상, 우, ..., 좌상
      dx= [0, 1, 1, 1, 0, -1, -1, -1] 
      dy= [-1, -1, 0, 1, 1, 1, 0, -1]
      ```


