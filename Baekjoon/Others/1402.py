T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print("yes")


''' 시간 초과 4
T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    A_tmp = []
    for j in range(1,(A + 1) // 2):
        if A % j == 0:
            if B == (A // j)+ j:
                print("yes")
                break
    else:
        print("no")

'''



'''
## 시간초과 3
T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    A_tmp = []
    for j in range(1,(A + 1) // 2):
        if A % j == 0:
            if B == (A // j)+ j:
                print("yes")
                break
    else:
        print("no")


## 시간초과 2
T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    A_tmp = []
    for j in range(1,(A + 1) // 2):
        if A % j == 0:
            A_tmp.append((A // j)+ j)
    #print(A_tmp)
    if B in A_tmp:
        print("yes")
    else:
        print("no")


## 시간초과
T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    A_tmp = []
    for j in range(1,(A + 1) // 2):
        if A % j == 0:
            A_tmp.append((A // j, j))
    #print(A_tmp)
    A_tmp2 = []
    for an in A_tmp:
        A_tmp2.append(sum(an))
    #print(A_tmp2)
    if B in A_tmp2:
        print("yes")
    else:
        print("no")

# A의 약수
# B의?'''