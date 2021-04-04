from math import sqrt

def solution(n, t, m, p):
    answer = ''
    order = 0
    break_chk = False
    number, length = 0, 1
    n_number = '0'

    while True:
        for i in range(length):
            order = (order + 1) % m
            if order == p%m:
                answer += n_number[i]
                t -= 1
            if t == 0:
                break_chk = True
                break
        if t == 0 or break_chk:
            break
        number += 1
        length, n_number = number_chk(number, n)

    return answer


def number_chk(number, n):
    table = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    if number == 0:
        return (1, '0')
    answer1 = ''
    answer2 = 1
    tmp_number = number
    while tmp_number > 0:
        answer1 += table[tmp_number % n]
        tmp_number //= n

    return (len(answer1), answer1[::-1])

