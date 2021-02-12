t = int(input())
for _ in range(t):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)
        continue

    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    # 내부원인지 외부원인지 확인
    if distance < max(r1,r2): #내부원
        if abs(r2-r1) == distance:
            print(1)
        elif abs(r2-r1) > distance:
            print(0)
        else:
            print(2)
    else:#외부원
        if r1 + r2 == distance:
            print(1)
        elif r1+ r2 < distance:
            print(0)
        else:
            print(2)

