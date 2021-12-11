import sys
# import time
# start = time.time()  # 시작 시간 저장

#input = sys.stdin.readline
#sys.stdin=open(".idea/inputs/11659_input1.txt","r")

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

dp_list = [0]*(n+1) #index 쉽게 접근
for i in range(1,n+1): #10만번
    dp_list[i] = dp_list[i-1] + n_list[i-1]

for _ in range(m):
    s, e = map(int, input().split())
    print(dp_list[e]-dp_list[s-1])



# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간