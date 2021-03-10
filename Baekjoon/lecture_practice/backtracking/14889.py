# n = int(input())
# s_ij = [list(map(int, input().split())) for i in range(n)]
# min_val = 100 * 20
#
# visit = [0] * n
# def comb(index=0, arr=[]):
#     if index == (n // 2):
#         global min_val
#         value = total_chk(arr)
#         if min_val > value:
#             min_val = value
#     else: #
#         tmp_index = arr[-1] if arr else index
#         for i in range(tmp_index, n):
#             if visit[i]: continue
#             visit[i] = 1
#             comb(index + 1, arr+[i])
#             visit[i] = 0
#
# def total_chk(arr):
#     total = 0
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             total += s_ij[arr[i]][arr[j]] + s_ij[arr[j]][arr[i]]
#     arr2 = list(set(range(n)) - set(arr))
#     total2 = 0
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             total2 += s_ij[arr2[i]][arr2[j]] + s_ij[arr2[j]][arr2[i]]
#     result = abs(total-total2)
#     return result
#
# comb()
# print(min_val)

from sys import stdin
from itertools import combinations

readline = stdin.readline
N = int(readline())
_map = [list(map(int, readline().split())) for _ in range(N)]

# 각 인원당 가능한 팀 스탯의 합
n_stat = [sum(i) + sum(j) for i, j in zip(_map, zip(*_map))]
print(list(zip(*_map)))
print(list(zip(_map,zip(*_map))))
print(n_stat)
# n_stat에는 인원 조합이 두번씩 들어감
all_stat = sum(n_stat) // 2
print(all_stat)
_min = 100 * N ** 2 + 1

# 팀을 절반으로 나눔
# 각 인원이 구성할 수 있는 모든 팀의 경우를
# combinations로 뽑는다.
# stat의 합을 all_stat에서 빼면 두 번 뺴지는 셀이 존재
# 두 번 빠지는 셀끼리 팀을 이루고, 그 외 인원들이 팀을 이룸
print(list(combinations(n_stat, N // 2)))
for stat in combinations(n_stat, N // 2):
    _min = min(_min, abs(all_stat - sum(stat)))

print(_min)