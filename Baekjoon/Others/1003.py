#fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
# fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
# 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
# fibonacci(0)은 0을 출력하고, 0을 리턴한다.
# fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
# 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.


#num    0   1
#0      1   0
#1      0   1
#2      1   1
#3      1   2
#4      2   3
#5      3   5 

#=>
T = int(input())
fibo_memoization = [0, 1,]

for tc in range(T):
    N = int(input())
    if N == 0:
        print(1, 0)
        continue
    try:
        print(fibo_memoization[N-1], fibo_memoization[N])
    except:
        for i in range(2,N+1):
            fibo_memoization.append(fibo_memoization[-1]+fibo_memoization[-2])
        print(fibo_memoization[N-1], fibo_memoization[N])

# 재귀:단점 ->속도가느리다. 깊이가 정해져있다.
# Dynamic Programming의 Memoization -> 메모이제이션 기법
# 적어둔다. fibo(4) = 0,1
# fibo= [0,1,1,2,3,5,8,]

