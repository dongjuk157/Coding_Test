def check_partition(a, b, _map):
    # 파티션이 모두 있는 경우 return True
    # 하나라도 없는 경우 return False
    # r1, r1 = a
    # r2, r2 = b
    if a[0] == b[0]:  # r1 == r2
        # 옆으로 두 칸 떨어져있는 경우 이므로 x의 중간 값으로 확인하면됨.
        if _map[a[0]][(a[1] + b[1]) // 2] == 'O':
            return False
    # else: # a[1] < b[1]
    elif a[1] == b[1]:
        # 위아래로 두칸 떨어져있는 경우 y의 중간값으로 확인
        if _map[(a[0] + b[0]) // 2][a[1]] == 'O':
            return False
    elif a[1] < b[1]:
        # a 기준으로 우측, 아래 확인
        if _map[a[0]][a[1] + 1] == 'O' \
                or _map[a[0] + 1][a[1]] == 'O':
            return False
    elif a[1] > b[1]:
        # a 기준으로 좌측, 아래 확인
        if _map[a[0]][a[1] - 1] == 'O' \
                or _map[a[0] + 1][a[1]] == 'O':
            return False
    return True


def distance_between(a, b):
    # a = r1, c1, b = r2, c2
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def check_distance_all(_map):
    # print(*_map, sep='\n')
    # 1 응시자 위치 파악
    map_size = 5
    p_list = []
    for i in range(map_size):
        for j in range(map_size):
            if _map[i][j] == 'P':
                p_list.append((i, j))
    # 응시자 끼리 거리 확인
    for i in range(len(p_list)):
        for j in range(i + 1, len(p_list)):
            # 맨해튼 거리가 2를 초과한 경우 continue
            dist = distance_between(p_list[i], p_list[j])
            if dist > 2:
                continue
            # 맨해튼 거리가 2 이하인 경우 파티션 확인
            if dist == 1 \
                    or not check_partition(p_list[i], p_list[j], _map):
                return 0
    return 1


def solution(places):
    answer = [1 for _ in range(len(places))]
    for i in range(len(places)):
        place = places[i]
        answer[i] = check_distance_all(place)

    return answer