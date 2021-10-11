# import sys; input = sys.stdin.readline

# N = int(input())
# cables = [tuple(map(int, input().split())) for _ in range(N)]
N = 8
cables = [(1, 8), (3, 9), (2, 2), (4, 1), (6, 4), (10, 10), (9, 7), (7, 6)]
answer = N
cables.sort(key=lambda x: x[0])
# print(cables)

# 두번째 전봇대에서 LIS 구하기(DP)
def binary_search(arr, l, r, target):
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return r

new_list = [0] + [e for s, e in cables]
d = []
for idx in range(1, N + 1):
    if not d or new_list[idx] > d[-1]:
        d.append(new_list[idx])
    else:
        tmp_i = binary_search(d, 0, len(d), new_list[idx])
        d[tmp_i] = new_list[idx]

print(N - len(d))

# print(answer)

