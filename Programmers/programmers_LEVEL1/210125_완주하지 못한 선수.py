# 타인의 코드
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (0.36ms, 10.3MB)
테스트 4 〉	통과 (0.81ms, 10.4MB)
테스트 5 〉	통과 (0.83ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (43.55ms, 24.3MB)
테스트 2 〉	통과 (67.15ms, 27.8MB)
테스트 3 〉	통과 (79.56ms, 30.2MB)
테스트 4 〉	통과 (106.45ms, 39.1MB)
테스트 5 〉	통과 (101.34ms, 39MB)
'''


def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for part in zip(participant, completion):
        if part[0] != part[1]:
            answer = part[0]
            break
    else:
        answer = participant[-1]
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.29ms, 10.3MB)
테스트 4 〉	통과 (0.79ms, 10.2MB)
테스트 5 〉	통과 (0.58ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (35.05ms, 18MB)
테스트 2 〉	통과 (65.83ms, 22.2MB)
테스트 3 〉	통과 (81.38ms, 24.8MB)
테스트 4 〉	통과 (89.96ms, 26.2MB)
테스트 5 〉	통과 (77.68ms, 26.2MB)
'''


def solution(participant, completion):
    answer = ''
    while completion != []:
        tmp = completion.pop()
        if tmp in participant:
            participant.remove(tmp)
        else:
            answer = tmp
            break
    else:
        answer = participant.pop()
    
    return answer
'''정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (2.00ms, 10.3MB)
테스트 4 〉	통과 (6.07ms, 10.2MB)
테스트 5 〉	통과 (6.28ms, 10.3MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
'''