# N, r, c = map(int, input().split())

# def recursive(N, r, c):
#     if N == 1:
#         return r * 2 + c
#     else:
#         full = 2 ** (N - 1)
#         half = 2 ** (N // 2)
#         if r < half and c < half:  # 0
#             return 0 * full + recursive(N - 1, r, c)
#         elif r < half:  # 1
#             return 1 * full + recursive(N - 1, r, c - half)
#         elif c < half:  # 2
#             return 2 * full + recursive(N - 1, r - half, c)
#         else:           # 3
#             return 3 * full + recursive(N - 1, r - half, c - half)
#
# for i in range(2 ** N):
#     for j in range(2 ** N):
#         print(recursive(2 ** N, i, j), end='\t')
#     print()
# print(recursive(2 ** N, r, c))

N, r, c = map(int, input().split())
def z(N, r, c):
    result = 0
    while N > 0:
        if N == 1:
            result += r * 2 + c
            break
        else:
            flag = 4 ** (N - 1)
            half = (2 ** N) >> 1
            N -= 1
            if r < half and c < half:
                continue
            elif r < half:
                result += flag
                c -= half
            elif c < half:
                result += flag * 2
                r -= half
            else:
                result += flag * 3
                r -= half
                c -= half
    return result

print(z(N, r, c))