#https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3

def solution(n):
    answer = 0
    rt_n=n**0.5
    #print((int(rt_n),rt_n))
    if (int(rt_n)==rt_n):
        answer = (rt_n + 1)*(rt_n + 1)
    else:
        answer = -1
    return answer

    