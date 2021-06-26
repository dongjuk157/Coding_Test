def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        skill_ind = 0
        for j in range(len(skill_trees[i])):
            tmp_ind = skill.find(skill_trees[i][j])
            if tmp_ind == -1: continue
            if tmp_ind == skill_ind:
                skill_ind += 1
            else:
                break
        else:
            answer += 1
    return answer