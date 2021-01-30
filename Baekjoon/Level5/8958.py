T = int(input())

for tc in range(T):
    tmp_list = input().split('X')
    result = 0
    for tmp in tmp_list:
        if tmp != '':
            result += sum(range(len(tmp)+1))
    print(result)