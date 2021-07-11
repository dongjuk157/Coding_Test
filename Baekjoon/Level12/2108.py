import sys; input = sys.stdin.readline
N = int(input())
# counting sort
count = [0] * 8001
total = 0
for i in range(N):
    num = int(input())
    count[num + 4000] += 1
    total += num

sa = []
fa = []
f = 0
for i in range(len(count)):
    if count[i]:
        sa.extend([i - 4000 for _ in range(count[i])])
        if f < count[i]:
            f = count[i]
            fa = [i - 4000]
        elif f == count[i]:
            fa.append(i - 4000)
# 산술평균, 중앙값, 최빈값, 범위
print(round(total/N), sa[N//2], fa[1] if len(fa) > 1 else fa[0], sa[-1] - sa[0], sep='\n')