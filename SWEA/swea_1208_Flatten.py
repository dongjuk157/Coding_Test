'''
메모리 56,860 kb / 실행시간 149 ms
'''
# 평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때,
# 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.


for test_case in range(1, 11):
    dump = int(input())
    heights_list = list(map(int, input().split()))
    
    while dump > 0: # 횟수제한
        # max를 찾아서 1을 빼고 min을 찾아서 1을 더함
        max_index = heights_list.index(max(heights_list))
        heights_list[max_index] -= 1
        min_index = heights_list.index(min(heights_list))
        heights_list[min_index] += 1
        
        dump -= 1
    
    print("#{0} {1}".format(test_case,max(heights_list)-min(heights_list)))
