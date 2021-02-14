def factorial(n):
    if n < 2:
        return 1
    else:
        return factorial(n-1)*n

n=int(input())
print(factorial(n))

##n==0일때도 판단해야한다.