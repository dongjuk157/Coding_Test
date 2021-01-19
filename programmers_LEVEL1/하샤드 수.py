#https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3

def solution(x):
    sum_x=0
    for i in str(x):
        sum_x+=int(i)
    answer = False if x%sum_x else True
    return answer