def getComb(numbers):
    all_comb_q = []
    all_comb = []
    q = []
    for num in numbers:
        q.append(num)
    while q:
        cur_num = q.pop(0)
        if cur_num >= 1000: continue
        tmp_len = len(str(cur_num))
        all_comb_q.append([cur_num, tmp_len])
        all_comb.append(cur_num)
        touch[cur_num] = tmp_len
        if cur_num == 0: continue
        for number in numbers:
            new_number = cur_num * 10 + number
            q.append(new_number)
    return all_comb, all_comb_q

T = int(input())
answer = ''
for tc in range(1, T + 1):
    N, O, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    goal = int(input())
    # 1. 숫자로 만들수 있는 모든 조합 반환
    touch = [-1 for _ in range(1000)]
    all_comb, all_comb_q = getComb(numbers)
    # print(all_comb)
    if touch[goal] != -1:
        answer += f'#{tc} {touch[goal]}\n'
        continue
    # 2. 백트래킹
    while all_comb_q:
        cur_num, cur_touch = all_comb_q.pop(0)
        if cur_num == goal:
            touch[goal] += 1
            break
        for num in all_comb:
            for op in operators:
                if op == 1: new_num = cur_num + num
                elif op == 2: new_num = cur_num - num
                elif op == 3: new_num = cur_num * num
                elif op == 4 and num:
                    new_num = cur_num // num

                if 0 <= new_num < 1000:
                    if touch[new_num] == -1 or touch[new_num] > cur_touch + touch[num] + 1:
                        touch[new_num] = cur_touch + touch[num] + 1
                        if touch[new_num] <= M:
                            all_comb_q.append([new_num, touch[new_num]])
    # 3. 값 반환
    if touch[goal] > M:
        touch[goal] = -1
    answer += f'#{tc} {touch[goal]}\n'
print(answer)