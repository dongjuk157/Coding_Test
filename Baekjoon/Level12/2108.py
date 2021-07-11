import sys; input = sys.stdin.readline
N = int(input())
# counting sort
count = [0] * 8001
total = 0
for i in range(N):
    num = int(input())
    count[num + 4000] += 1
    total += num

index = 0
mid = 0
mid_chk = False
min_val = 0
min_chk = False
max_val = 0
for i in range(len(count)):
    if count[i]:
        index += count[i]
        max_val = i - 4000
        if not mid_chk and index > N // 2:
            mid_chk = True
            mid = i - 4000
        if not min_chk:
            min_chk = True
            min_val = i - 4000
tmp = max(count)
tmp_arr = [i - 4000 for i in range(len(count)) if count[i] == tmp]


# 산술평균, 중앙값, 최빈값, 범위
print(round(total/N), mid, tmp_arr[1] if len(tmp_arr) > 1 else tmp_arr[0] , max_val - min_val, sep='\n')