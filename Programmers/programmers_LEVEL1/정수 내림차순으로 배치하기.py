#https://programmers.co.kr/learn/courses/30/lessons/12933
def solution(n):
    answer = 0
    n=list(sorted(str(n),reverse=True))
    answer=int(''.join(n))
    
    #m=list(str(n))
    #m.sort()
    #m.reverse()
    #for i in m:
    #    tmp+=(i)
    #answer=int(tmp)
    return answer