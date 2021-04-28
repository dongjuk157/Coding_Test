# import sys
# input = sys.stdin.readline
#
# want_ch = input().rstrip()
# want_ch_list = list(map(int, list(want_ch)))
# want_ch = int(want_ch)
# use_set = set(range(10))
# M = int(input())
# if M:
#     crashed_set = set(map(int, input().split()))
#     use_set = use_set - crashed_set
#
#
# result = 500000
# min_distance = 500000
# min_dist_val = -1
# def backtrack(ind=0, cur_ch=100, index=0):
#     global result, min_distance, min_dist_val
#     if cur_ch == want_ch:
#         result = min(result, ind)
#         min_distance = 0
#         return
#
#     dist = abs(cur_ch - want_ch)
#     if min_distance > dist:
#         min_distance = dist
#         min_dist_val = cur_ch
#         result = ind if ind else result
#     elif min_distance == dist:
#         if min_dist_val > cur_ch:
#             min_dist_val = cur_ch
#             result = ind
#         elif min_dist_val == cur_ch:
#             if result > ind:
#                 result = ind
#
#     if index == len(want_ch_list) + 1:
#         return
#         ### index에서 하나더 가는경우까지 조사
#
#     for num in list(use_set):
#         if index == 0:
#             # if num == 0: continue
#             cur_ch = 0
#         backtrack(ind + 1, cur_ch * 10 + num, index + 1)
#
# backtrack()
# # print(result, min_distance)
# print(min(result + min_distance, abs(100 - want_ch)))


