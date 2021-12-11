n = int(input())
numbers = list(map(int, input().split()))
answer = [-1] * n
val = 0
stack = []
for i in range(n - 2, -1, -1):
    tmp = numbers.pop()
    stack.append(tmp)
    # 1. 값 두개 비교. 오른쪽 값이 크면 해당 값 저장
    if numbers[i] < tmp:
        val = tmp
    if numbers[i] >= val:
        while stack:
            val = stack.pop()
            if numbers[i] < val:
                answer[i] = val
                stack.append(val)
                break
    else:
        answer[i] = val

print(*answer)