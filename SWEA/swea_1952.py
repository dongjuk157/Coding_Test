import sys
sys.stdin = open('.idea/1952_input.txt','r')

for tc in range(1, int(input()) + 1):
    prices = list(map(int, input().split()))
    months = [0]+list(map(int, input().split()))
    total_price = [0] * 13
    for i in range(1, 13):
        tmp0 = total_price[i - 1] + months[i] * prices[0]
        tmp1 = total_price[i - 1] + prices[1]
        total_price[i] = min(tmp0, tmp1)
        if i < 3: continue
        tmp2 = total_price[i - 3] + prices[2]
        total_price[i] = min(total_price[i], tmp2)
    min_total_price = min(total_price[12],prices[3])
    print("#{} {}".format(tc, min_total_price))



