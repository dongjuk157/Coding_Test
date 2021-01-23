'''
메모리 59,244 kb / 실행시간155 ms
'''

T = 10
for test_case in range(1, T + 1):
    len_building = int(input())
    building = list(map(int, input().split()))
    building_ok = 0 #조망권이 확보된 세대의 수
    
    for index in range(2, len_building-2):		# index = 2~97, (index가 0,1, -1,-2인 곳은 높이가 항상 0임)
        # 비교해야 할 곳은 총 왼쪽 둘 오른쪽 둘 
        if building[index] < building[index-1]:
            continue
        if building[index] < building[index-2]:
            continue
        if building[index] < building[index+1]:
            continue
        if building[index] < building[index+2]:
            continue
       	# 조망권이 확보된 건물이면 세대수 측정
        building_ok += building[index] - max(building[index-1], building[index-2], building[index+1], building[index+2])
        
    print("#{0} {1}".format(test_case,building_ok))




'''
닉네임: 꼬동 / 메모리 50,728 kb / 실행시간 138 ms

for tc in range(10):
    N = int(input())
    buildings = list(map(int,input().split()))
    cnt = 0
    index = 2
    while index < N - 2:
        bu_5 = buildings[index-2:index+3]
        if buildings[index] != max(bu_5):
            index += 1
            continue
        else:
            cnt += sorted(bu_5)[-1] - sorted(bu_5)[-2]
            index += 3
    print('#{} {}'.format(tc + 1, cnt))

'''