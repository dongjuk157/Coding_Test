'''
메모리 59,232 kb / 실행시간 144 ms
'''

# 최빈수를 출력하는 프로그램을 작성
# 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력

T = int(input())        # 첫 번째 줄에 테스트 케이스의 수 T가 주어짐
for test_case in range(1, T + 1):
    # 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어짐
    # 그 다음 줄부터는 점수가 주어짐. 테스트 케이스의 점수를 리스트로 저장
    tc_num=int(input())
    scores = list(map(int,input().split())) 

    mode = {}           # dictionary로 저장해서 {score: num_of_mode}, mode: 최빈값
    
    for score in scores:
        if mode.get(score):         # 딕셔너리에 key가 있는 경우
            mode[score] += 1
        else:                       # 딕셔너리에 key 없는경우
            mode[score] = 1

    
    max_key, max_value = 0, 0           # 최빈값과 그 값이 나타난 횟수
    for key in mode:                    # 딕셔너리는 key가 중복되지 않으므로 횟수로 비교
        if mode[key] > max_value:       # 횟수가 큰 경우 max_key, max_value 교체
            max_value = mode[key]    
            max_key = key
        elif mode[key] == max_value:    # 횟수가 같은 경우 최빈값(key값)이 큰 경우만 교체
            if max_key < key:
                max_key = key
                
    print("#{0} {1}".format(tc_num,max_key))
