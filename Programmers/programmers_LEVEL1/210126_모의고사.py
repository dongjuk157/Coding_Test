def solution(answers):
    answer = []
    stud1 = [1,2,3,4,5]
    stud2 = [2,1,2,3,2,4,2,5] 
    stud3 = [3,3,1,1,2,2,4,4,5,5]
    score1 = 0
    score2 = 0
    score3 = 0

    for i in range(len(answers)):
        if stud1[i%5] == answers[i]:
            score1 += 1
        if stud2[i%8] == answers[i]:
            score2 += 1
        if stud3[i%10] == answers[i]:
            score3 += 1
    
    max_score = max([score1,score2,score3])
    if max_score == score1:
        answer.append(1)
    if max_score == score2:
        answer.append(2)
    if max_score == score3:
        answer.append(3)

    return answer