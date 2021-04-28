n = int(input())
numbers = [int(input()) for _ in range(n)]
stack = []
result_list = []
num = 1
result = 0
while num <= n or stack:
    if num > n:
        if stack[-1] == numbers[result]:
            result += 1
            stack.pop()
            result_list.append('-')
        else:
            break
    elif stack and stack[-1] == numbers[result]:
        result += 1
        stack.pop()
        result_list.append('-')
    else:
        stack.append(num)
        num += 1
        result_list.append('+')
if stack:
    print("NO")
else:
    print(*result_list, sep='\n')


# push, 1       []
# push, 12      []
# push, 123     []
# push, 1234    []
# pop,  123     4
# pop,  12      43
# push, 125     43
# push, 1256    43
# pop,  125     436
# push, 1257    436
# push, 12578   436
# pop,  1257    4368
# pop,  125     43687
# pop,  12      436875
# pop,  1       4368752
# pop   []      43687521