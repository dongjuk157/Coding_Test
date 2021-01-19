#https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    len_pn=len(phone_number)-4
    answer = '*'*len_pn+phone_number[-4:]
    return answer