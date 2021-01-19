#https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s): #_try hello world" ,"try hello world"
    answer = ''
    words= s.split(' ') 
    print(words)
    for word in words:
        cnt=0
        for char in word:
            if char.isalpha():
                cnt+=1
                if cnt%2:
                    answer+=char.upper()
                else:
                    answer+=char.lower()
            else:
                answer+=char
        answer+=' '
        print(answer)
    return answer[:-1]