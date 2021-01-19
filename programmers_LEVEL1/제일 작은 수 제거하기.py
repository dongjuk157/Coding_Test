#https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    answer=[]
    min_arr=min(arr)
    answer = [i for i in arr if i > min_arr]
    #[i for i in arr if i > min(arr)] 으로 했을때 시간초과
    # if 문에서 min을 계속 찾다보니 시간 복잡도가 높아지는것 같다.
    if answer == []:
        answer.append(-1)
    return answer