for tc in range(int(input())):
    player = [0] * 11
    for i in range(11):
        player[i] = list(map(int,input().split()))
    visit = [0] * 11
    max_val = 0
    def comb(index=0, total=0):
        if index == 11:
            global max_val
            if max_val < total:
                max_val = total
        else:
            for i in range(11):
                if not player[i][index] or visit[i] == 1: continue
                visit[i] = 1
                comb(index+1, total+player[i][index])
                visit[i] = 0

    comb()
    print(max_val)
