factorial = [1, 1, ]  # 0!, 1!

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    for number in range(len(factorial), m + 1):
        factorial.append(factorial[-1] * number)
    # print(factorial)
    result = factorial[m] // (factorial[n] * factorial[m - n])  # mCn
    print(result)
