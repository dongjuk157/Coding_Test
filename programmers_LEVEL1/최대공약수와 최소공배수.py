#https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    #initial settings
    if n>m: # m is always bigger
        n,m=m,n
    tmp_big=m       
    tmp_small=n
    gcd=tmp_big%tmp_small
    
    
    #최대 공약수, Euclid algorithm, m=n*i+x -> m'=n, n'=x -> ...
    while (gcd):#나머지가 있으면
        tmp_big= tmp_small
        tmp_small=gcd
        gcd=tmp_big%tmp_small
    answer.append(tmp_small)
    
    #최소 공배수
    answer.append(n*m/(answer[0]))

    return answer