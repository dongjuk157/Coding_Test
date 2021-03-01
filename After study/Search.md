# 검색 Search

저장되어 있는 자료 중에서 원하는 항목을 찾는 작업. 

목적하는 탐색 키를 가진 항목을 찾는 것.

- 탐색 키(search key): 자료를 구별하여 인식할 수 있는 키



### 순차검색 Sequential Search

일렬로 되어있는 자료를 순서대로 검색하는 방법

배열이나 연결리스트(linked list) 등 순차 구조로 구현된 자료구조에서 원하는 항목을 찾을때 유용함

알고리즘이 단순하지만 검색대상이 많은경우 시간 복잡도가 급격히 증가함



**정렬되어 있지 않은 경우 ** 

- 시간복잡도 O(n) <- (1+2+3+...+n)/n
- 첫번째 원소부터 순서대로 키값이 있는지 비교함
- 키값이 동일한 원소가 있으면 인덱스를 반환하고, **마지막까지 없으면 검색 실패**
- 찾고자 하는 원소의 순서에 따라 비교 회수가 결정됨(첫번째원소의 경우 1번 비교, 두번째원소 2번비교)



**정렬된 경우**(오름차순 가정)

- 시간복잡도 O(n)
- 자료를 순차적으로 검색하면서 **원소의 키 값이 검색 대상의 키값보다 크면 바로 종료**
- 정렬이 되어있으므로 검색 실패를 반환하는 경우 평균 비교회수가 반으로 줄어듦



### 이진탐색 Binary Search

자료의 가운데에 있는 항목의 키값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

목적 키를 찾을때까지 이진검색을 순환적으로 반복수행함

**정렬된 상태**여야하므로, 자료에 삽입이나 삭제가 발생했을때 항상 정렬하는 작업이 필요함

검색 과정

1. 자료의 중앙에 있는 원소를 고름
2. 중앙원소의 값과 찾고자 하는 목표값을 비교함
3. 목표값이 중앙원소의 값보다 작으면 자료의 왼쪽 반, 크면 오른쪽 반에 대해서 새로 검색을 수행함.

```python
def binarySearch(a, key):
    start = 0
    end = len(a) -1
    while start <= end:
        middle = (start + end)//2
        
        if a[middle] == key:
            return True
        
        elif a[middle] > key:
            end = middle - 1
            
        else:
            start = middle + 1
	return False
```

```python
#재귀함수
def binarySearchRecursive(a,low,high,key):
    
    if low> high:
        return False
    
    else:
        middle = (low + high) // 2
        if a[middle] == key:
            return True
        
        elif a[middle] > key:
            return binarySearchRecursive(a, low, middle - 1, key)
        
        else:
            return binarySearchRecursive(a, middle + 1, high, key)
```



### 해쉬

시간복잡도는 좋음

공간복잡도가 증가함

구현이 어려움.



### 인덱스

db에서 많이 씀