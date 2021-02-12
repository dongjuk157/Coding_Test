import sys
import time

#n = int(input())
#n=10000000

for n in range(1,10000000):
    i = 2
    while (n >= i * i):
        if n % i == 0:
            n //= i
            print(i)
        else:
            i += 1
    if n != 1:
        print(int(n))



