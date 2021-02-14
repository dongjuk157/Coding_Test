def hanoi(disk, start, mid, end):
    if disk == 1: #목적지로 옮기기 위해
        print(start, end)
    else:
        hanoi(disk - 1, start, end, mid)    # 2**(n-1)  n-1개를 mid에 옮김
        print(start, end)                   # 1         가장밑에있는 것을 end로 옮김
        hanoi(disk - 1, mid, start, end)    # 2**(n-1)  mid에 있는걸 다시 end로 옮김

n = int(input())
print(2**n - 1)
hanoi(n, 1, 2, 3)