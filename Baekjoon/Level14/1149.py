N = int(input())
total = [[0]*3 for _ in range(N + 1)]

for i in range(1, N + 1):
    x, y, z = list(map(int, input().split()))
    if i == 1:
        total[i] = [x, y, z]
    else:
        total[i][0] = min(total[i - 1][1], total[i - 1][2]) + x
        total[i][1] = min(total[i - 1][0], total[i - 1][2]) + y
        total[i][2] = min(total[i - 1][1], total[i - 1][0]) + z
print(min(total[N]))



