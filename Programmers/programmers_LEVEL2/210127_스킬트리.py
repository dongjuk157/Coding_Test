def solution(skill, skill_trees):
    answer = 0 

    for skill_tree in skill_trees:
        old_val = skill_tree.find(skill[0])     # 이전값과 비교하기 위한 변수. 처음 값은 skill의 첫 글자의 인덱스값
        for sk in skill[1:]:                    
            val = skill_tree.find(sk)           # val는 비교할 값의 인덱스 

            if old_val == -1:                   # 만약 old_val == -1 인 경우에는(스킬트리 내에 없음)
                if val != -1:                   #   다음값이 다 -1인 경우(스킬트리에 없는 경우)에만 진행
                    break                       #   하나의 값이 존재하면 불가능한 스킬트리
            else: # old_val > -1                # 이전값이 스킬트리 내에 있고
                if val < old_val:               #   현재 값이 이전값보다 작은 경우
                    if val == -1:               #     현재값이 스킬트리 내 없으면 가능
                        old_val = val
                    else:                       #     스킬트리내 있으면 불가능
                        break
                else:                           #   현재값이 이전값보다 큰 경우는 가능
                    old_val = val               
        else:
            answer += 1                         # break없이 돌았을경우 가능한 스킬트리
    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
'''

## 다른 사람의 풀이. 깔끔해서 가져왔다.
from collections import deque
def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = deque(list(skill))
        for s in skill_tree:
            if s in skill:
                if s != skill_list.popleft():
                    break
        else:
            answer += 1

    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
'''

