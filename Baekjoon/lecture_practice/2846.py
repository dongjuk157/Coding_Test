n=int(input())
h=list(map(int,input().split()))
result = [[0],]
tmp = []
for i in range(1, n):
    if h[i-1] < h[i]:
        tmp.append(h[i-1])
    else:
        tmp.append(h[i-1])
        result.append(tmp)
        tmp = []
else:
    tmp.append(h[-1])
    result.append(tmp)
max_num = 0
for r in result:
    if max_num < r[-1] - r[0]:
        max_num = r[-1] - r[0]
print(max_num)
