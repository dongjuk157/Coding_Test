dice=list(map(int,input().split()))
lsd = len(set(dice))
if lsd == 1:
    print(10000+dice[0]*1000)
elif lsd == 3:
    print(max(dice)*100)
else:
    tmp = dice.pop()
    if tmp == dice[-1] or tmp == dice[0]:
        print(1000+100*tmp)
    else :
        print(1000+100*dice[0])