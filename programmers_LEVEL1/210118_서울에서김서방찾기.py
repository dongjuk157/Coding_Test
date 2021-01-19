#https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    #반드시 Seoul 안에 포함되어있기때문에 index 사용
    index= seoul.index('Kim')
    answer = '김서방은 '+ str(index)+'에 있다'
    return answer