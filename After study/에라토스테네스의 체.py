def prime_number(N):
    # 0,1은 소수가 아니므로 False로 선언하고 나머지는 True로 선언
    prime = [False,False]+[True for i in range(N+1)] 

    for i in range(2, int(N**0.5) + 1):
    #2부터 n의 제곱근까지의 모든 수를 확인
        if prime[i] == True: # 소수인 경우
            # i를 제외한 i의 모든 배수를 지우기
            j = 2 
            while i * j <= N: 
                prime[i * j] = False
                j += 1

    # 배열에서 True인 index만 반환. index == number, 즉 소수만 반환
    return [ i for i in range(2, N+1) if prime[i] ]


print(prime_number(100))