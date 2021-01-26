def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]
 
def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concatenate(x, x)
    b = concatenate(x, [' '*n]*n)
 
    return a + b + a
 
print('\n'.join(star10(int(input()))))


'''
이거랑 생각은 똑같이 했는데
구현하기가 너무 어려웠다...
더 열심히 해야할듯...

'''