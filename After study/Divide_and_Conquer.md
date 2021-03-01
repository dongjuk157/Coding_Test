# 분할 정복 Divide and Conquer

기본적으로는 엄청나게 크고 방대한 문제를 조금씩 조금씩 나눠가면서 용이하게 풀 수 있는 문제 단위로 나눈 다음 그것들을 다시 합쳐서 해결하자는 개념

- 분할: 문제를 동일한 유형의 여러 하위 문제로 나눈다.
- 정복: 가장 작은 단위의 하위 문제를 해결하여 정복한다.
- 조합: 하위 문제에 대한 결과를 원래 문제에 대한 결과로 조합한다.



Ex 거듭제곱

```python
def recursive_power(x,n):
    if n == 1: return x
    if n & 1:
        y = recursive_power(x,(n-1)//2)
        return y*y*x
    else:
        y = recursive_power(x,n//2)
        return y*y
```



Ex2 퀵정렬

작은 부분, 큰 부분으로 계속 나누어서 정렬