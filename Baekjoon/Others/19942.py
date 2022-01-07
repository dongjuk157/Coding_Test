# import sys; input = sys.stdin.readline

def list_chk(lst, goal, foods):
    # 최저 영양소 기준을 만족하는지 체크
    sum_val = [0 for _ in range(5)]
    for i in range(5):
        for j in range(len(lst)):
            sum_val[i] += foods[lst[j]][i]

        if i == 4: continue
        if sum_val[i] < goal[i]:
            return (False, None)

    return (True, sum_val[4])

def backtrack(ind, limit, foods, goal, lst=[]):
    list_answer_chk = list_chk(lst, goal, foods)
    if list_answer_chk[0]:
        global answer
        answer.append((list_answer_chk[1], lst))
        return
    if ind == limit:
        return
    backtrack(ind+1, limit, foods, goal, lst+[ind])
    backtrack(ind+1, limit, foods, goal, lst)

def main():
    N = int(input())
    goal = tuple(map(int, input().split()))
    foods = [tuple(map(int, input().split())) for _ in range(N)]
    # foods.sort(key=lambda x:(x[4]))
    global answer
    answer = []
    backtrack(0, N, foods, goal)
    if answer:
        answer.sort(key=lambda x:(x[0], ''.join(map(str, map(lambda y: y+1, x[1])))))

        print('{}\n{}'.format(answer[0][0],' '.join(map(str, map(lambda y: y+1,answer[0][1])))))
    else:
        print(-1)



if __name__ == '__main__':
    main()