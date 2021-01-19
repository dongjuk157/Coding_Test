'''https://programmers.co.kr/learn/courses/30/lessons/12943?language=python3

'''

def solution(num):
    answer = 0
    while num!=1:
        if num%2: ##odd
            num=num*3+1
        else: ##even
            num/=2
        answer+=1
        if answer==500:
            answer=-1
            break
    return answer