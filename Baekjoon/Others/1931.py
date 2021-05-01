N = int(input())
time = []
for _ in range(N):
    s, e = map(int, input().split())
    time.append((s, e))
time.sort(key=lambda x:(x[1], x[0]))
result = 0
last = 0
for i in range(N):
    if last <= time[i][0]:
        result += 1
        last = time[i][1]
print(result)