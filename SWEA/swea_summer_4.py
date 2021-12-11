import sys
sys.stdin = open('swea_summer_4.txt','r')
# T = int(input())
# for tc in range(1, T + 1):
#     # 입력
#     initial = input()
#     destination = input()
#     anticlock_weight = [1, 2, 4, 6]
#     clock_weight = [1, 3, 5, 7]
#     END = ord('Z')
#     START = ord('A')
#
#     result = 0
#     for i in range(len(initial)):
#         left, right = 0, 0
#         if ord(initial[i]) == ord(destination[i]):
#             continue
#         elif ord(initial[i]) < ord(destination[i]):
#             right = ord(destination[i]) - ord(initial[i])
#             left = ord(initial[i]) - ord(destination[i]) + END - START + 1
#         else:
#             right = ord(destination[i]) - ord(initial[i]) + END - START + 1
#             left = ord(initial[i]) - ord(destination[i])
#
#         # 가중치를 곱했을 경우 더 작은 값을 result 에 가산
#         result += min(left * clock_weight[i], right * anticlock_weight[i])
#     print("#{} {}".format(tc, result))

## 2번
T = int(input())
for tc in range(1, T+1):
    # 입력
    initial = input()
    destination = input()
    # 가중치도 받고 자물쇠에 있는 알파벳도 받으면 조금 심화 버전일듯
    # 자물쇠에있는 알파벳은 현재  ABCD...Z까지 있는데 이걸 "AABSDGHASFAH" 이런식으로 무작위?
    anticlock_weight = [1, 2, 4, 6]
    clock_weight = [1, 3, 5, 7]
    END = ord('Z') + 1
    START = ord('A') - 1

    result = 0
    for i in range(len(initial)):
        # 1 왼쪽으로 가는 경우 계산
        left = 0
        j = ord(initial[i])
        while chr(j) != destination[i]:
            left += 1
            j -= 1
            if j == START:
                j = END
                left -= 1

        # 2 오른쪽으로 가는 경우 계산
        right = 0
        j = ord(initial[i])
        while chr(j) != destination[i]:
            right += 1
            j += 1
            if j == END:
                j = START
                right -= 1
        # 가중치를 곱했을 경우 더 작은 값을 result 에 가산
        result += min(left*clock_weight[i], right*anticlock_weight[i])
    print("#{} {}".format(tc, result))