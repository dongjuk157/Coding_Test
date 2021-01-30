C = int(input())

for tc in range(C):
    tmp = list(map(int,input().split()))
    N, scores = tmp[0] , tmp[1:]
    aver = sum(scores) / N
    rates = len([score for score in scores if score > aver])/N * 100

    print("{0:.3f}%".format(rates))