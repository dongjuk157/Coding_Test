# N번째 손님 => N//H +1 호, N % H  층
# 10 번째 손님 => 10//6 +1 = 2호,  4 층
# 72 번째 손님 => 72//30 +1 = 3호, 12 층


T = int(input()) # 테스트 데이터 개수

for i in range(T):
    H, W, N = map(int,input().split())
    
    result = ((N % H) * 100) + ((N // H) + 1) if N % H !=0 else (H * 100) + (N // H)

    print(result)

# 몫, 나머지를 사용할땐 0인 케이스를 확인하자