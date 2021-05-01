#N-54 ~N-1중에 만들수있는지 확인

N=int(input())
result = 0
for i in range(max(1, N - 9 * len(str(N))), N):
    ssj = i + sum(map(int, list(str(i))))
    if ssj == N:
        print(i)
        break
else:
    print(0)



# N = int(input())
# for i in range(1,1000001):
#     ssj = i + sum(map(int, list(str(i))))
#     if ssj == N:
#         print(i)
#         break
# else:
#     print(0)
