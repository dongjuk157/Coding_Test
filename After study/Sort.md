# 정렬

### Stable Sort

동일한 값을 가지는 원소들의 순서가 정렬된 후에도 유지되는 정렬

- 버블 정렬
- 카운팅 정렬
- 삽입 정렬
- 병합 정렬



### unstable sort

동일한 값을 가지는 원소들의 순서가 정렬된 이후에도 유지되지 않는 정렬

- 선택 정렬
- 힙 정렬
- 퀵 정렬
- 쉘 정렬



### In-place Algorithm

원소들의 개수에 비해서 충분히 무시할 만한 저장 공간만을 더 사용하는 정렬 알고리즘

- 버블 정렬, 선택 정렬, 삽입 정렬, 힙 정렬, 쉘 정렬
- 퀵 정렬(정의에 따라서 Not in place sorting으로 볼수있음)

**Not-in-place**

- 카운팅, 기수(Radix), 합병, 버켓 정렬



## 정렬 알고리즘

### 버블 정렬

시간복잡도 O(n^2)

- 인접한 두개의 원소를 비교하면서 자리를 계속 교환하는 방식
- 첫번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 마지막 자리까지 이동.

```python
def bubble(_list):
    for i in range(len(_list)-1):
        for j in range(0,i):
	        if _list[j] < _list[j+1]:
    	        _list[j], _list[j+1] = _list[j+1], _list[j]
```



### 선택 정렬

시간 복잡도 O(n^2)

- 저장되어있는 자료로 부터 k 번째로 큰, 작은 원소를 찾아서 정렬하는 방식

- 교환횟수가 버블, 삽입 정렬보다 적음

```python
def selectionSort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i+1, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
```

- 셀렉션 알고리즘을 전체 범위로 확장한 것

-  셀렉션 알고리즘

  - 저장되어있는 자료로 부터 k 번째로 큰, 작은 원소를 찾는 방법(최대값, 최소값, 중간값 등을 찾음)

    ```python
    # k 번째로 작은 원소를 찾는 알고리즘
    def select(_list, k):
        for i in range(k):
            # 1. 최소값을 찾음
            min_index = i
            for j in range(i+1, len(_list)):
                if _list[min_index] > _list[j]:
                    min_index = j
            # 2. 최소값과 맨 앞값을 바꿈(차례대로 바꿈)
            _list[i],_list[min_index] = _list[min_index],_list[i]
        return list[k-1] #3. k번 반복했으니 마지막에 찾은 값 리턴
    ```

    - 시간복잡도 O(k*n)




### 카운팅 정렬

시간복잡도 O(n+k), n:배열의 크기, k: 배열의 최대값

- 항목들의 순서를 결정하기 위해 집합게 각 항목이 몇개씩 있는지 세는 작업을 함,
- 선형시간에 정렬하는 효율적인 알고리즘
- 카운트들을 위한 충분한 공간을 할당하려면 집합내의 가장 큰 정수를 알아야함
- 크기에 영향을 받고 메모리를 추가로 사용함
- 제한 사항: 정수나 정수로 표현할수 있는 자료에 대해서만 적용 가능.

```python
# 정렬 방식 설명
# n: 배열의 크기 8, k: 배열의 최대값 4
notsort = [0,4,1,3,1,2,4,1]
sort_arr = [0] * n #초기화
# 1 원소별 cnt
cnt = [1,3,1,1,2] 

# 2 => count를 누적한 값으로 조정 
for i in range(1, n):
    cnt[i] += cnt[i - 1]
# cnt=[1,4,5,6,8]

# 3 뒤에서부터 순회하며 새로운 배열에 정렬
for i in range(n):
    cnt[notsort[n - i - 1]] -= 1
    sort_arr[cnt[notsort[n - i - 1]]] = notsort[n - i - 1]
#notsort[-1]==1, cnt[1]을 감소시키고(cnt[1]->3) sort[3]에 1 삽입
#count= [1,3,5,6,8]
#sort=[0,0,0,1,0,0,0,0]

#notsort[-2]==4, cnt[4]를 감소시키고(cnt[4]->7) sort[7]에 4 삽입
#count= [1,3,5,6,7]
#sort=[0,0,0,1,0,0,0,4]

#notsort[-3]==2, cnt[2]를 감소시키고(cnt[2]->4) sort[4]에 2 삽입
#count= [1,3,4,6,7]
#sort=[0,0,0,1,2,0,0,4]

#notsort[-4]==1, cnt[1]를 감소시키고(cnt[1]->2) sort[2]에 1 삽입
#count= [1,2,4,6,7]
#sort=[0,0,1,1,2,0,0,4]

#notsort[-5]==3, cnt[3]를 감소시키고(cnt[3]->5) sort[5]에 3 삽입
#count= [1,2,4,5,7]
#sort=[0,0,1,1,2,3,0,4]

#notsort[-6]==1, cnt[1]를 감소시키고(cnt[1]->1) sort[1]에 1 삽입
#count= [1,1,4,5,7]
#sort=[0,1,1,1,2,3,0,4]

#notsort[-7]==4, cnt[4]를 감소시키고(cnt[4]->6) sort[6]에 4 삽입
#count= [1,1,4,5,6]
#sort=[0,1,1,1,2,3,4,4]

#notsort[-8]==0, cnt[0]를 감소시키고(cnt[0]->0) sort[0]에 0 삽입
#count= [0,1,4,5,6]
#sort=[0,1,1,1,2,3,4,4]

#마지막 원소까지 정렬하면 sort를 반환
```

```python
# 생각나서 적어보는 정렬 방식, cnt누적 안해도 되는 방식
notsort = [0,4,1,3,1,2,4,1] 
sort_arr = [0] * len(notsort)
# 1 원소별 cnt
cnt = [1,3,1,1,2] 

# 2 cnt수 만큼 차례대로 정렬
for i in range(len(cnt)):
    sort_arr.extend([i]*cnt[i])
# 2-1 cnt[0] == 1 이므로 0 하나 추가
#sort = [0]

# 2-2 cnt[1] == 3 이므로 1 세 개 추가
#sort =[0,1,1,1]

#cnt끝까지 반복
#sort = [0,1,1,1,2,3,4,4]
```

- 누적합 counting sort 는 stable 하게 만들어 줌. 
  - radix sort 시 LSB 순서로 정렬할 경우 이전에 정렬한 값을 다음 정렬시에도 반영하여 정렬할 수 있음



#### Radix sort

기수 별로 비교 없이 수행하는 정렬 알고리즘

크기가 유한하고 사전순으로 정렬할 수 있어야 함

부동소수점 실수처럼 특수한 비교 연산이 필요한 데이터에는 적용할 수 없음

사용 가능할 때에는 매우 좋은 알고리즘

```python
# 카운팅 정렬 기반으로 사용함
def countingSort(arr, exp1):   
    n = len(arr) 
    output = [0] * n 
    count = [0] * (10) 	    # 각 자리수끼리 비교하므로 0~9까지만 확인하면됨
    for i in range(0, n):   # count 계산
        index = (arr[i] / exp1) 
        count[int(index % 10)] += 1
    for i in range(1, 10):  # 누적 합 계산
        count[i] += count[i - 1] 
  
    i = n - 1
    while i >= 0: 
        index = (arr[i] / exp1) 
        output[count[int(index % 10)] - 1] = arr[i] 
        count[int(index % 10)] -= 1
        i -= 1
        
    i = 0
    for i in range(0, len(arr)): 
        arr[i] = output[i] 
  
# Method to do Radix Sort 
def radixSort(arr): 
    max1 = max(arr) 
    exp = 1				
    # 1의 자리부터 시작해서 최대 자리수까지 반복하며 정렬
    while max1 / exp > 0: 
        countingSort(arr, exp) 
        exp *= 10
        
# Driver code 
arr = [170, 45, 75, 90, 802, 24, 2, 66] 
  
# Function Call 
radixSort(arr) 
  
for i in range(len(arr)): 
    print(arr[i])   
```



### 삽입 정렬



### 병합 정렬



### 퀵 정렬

분할 정복으로 수행하는 알고리즘

```python
def quicksort(arr, low, high):
    if high <= low:
        return arr

    mid = partition(arr, low, high)
    quicksort(arr, low, mid - 1)
    quicksort(arr, mid, high)

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1
    return low
```





---

참고한 글

[stable, inplace](https://velog.io/@cookncoding/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B0%9C%EB%85%90-Stable-Sort-Inplace)

[Wikipedia Radix sort Example](https://en.wikipedia.org/wiki/Radix_sort#Examples)