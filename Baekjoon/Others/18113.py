# import sys; input = sys.stdin.readline

def remove_kkodari(dist, K):
    if dist <= K:
        return 0
    dist -= K
    if dist >= K:
        dist -= K
    return dist

def binarySearch(kimbab, limit, max_val):
    if not kimbab:
        return -1
    answer = -1
    s, e = 0, max_val
    while s <= e:
        p = (s + e) // 2
        if p == 0:
            s = 1  # s = p + 1
            continue

        # tmp_num: 김밥 조각의 개수
        tmp_num = sum(map(lambda x: x // p, kimbab))

        # 작으면 자르는 길이를 줄이는 방향
        if tmp_num < limit:
            e = p - 1

        # 많거나 같으면 자르는 길이를 키우는 방향
        else:
            s = p + 1
            answer = p

    return answer



def main():
    # 0 input
    N, K, M = map(int, input().split())

    # 1 remove kkodari
    kimbab = []
    max_val = 0
    for _ in range(N):
        tmp = remove_kkodari(int(input()), K)
        if tmp:
            kimbab.append(tmp)
            max_val = max(tmp, max_val)

    # 2 binarySearch and output
    print(binarySearch(kimbab, M, max_val))


if __name__ == '__main__':
    main()
