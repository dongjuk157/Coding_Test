n,m = map(int,input().split())

def num_5(n):
    count = 0
    while n != 0:
        n = n // 5
        count += n 
    return count

def num_2(n):
    count = 0
    while n != 0:
        n = n // 2
        count += n
    return count

total_2 =  num_2(n) - num_2(m) - num_2(n-m)
total_5 = num_5(n) - num_5(m) - num_5(n-m)

answer = min(total_2, total_5)
print(answer)
