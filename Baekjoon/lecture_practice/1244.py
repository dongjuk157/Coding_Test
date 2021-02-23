import sys
#input = sys.stdin.readline
sys.stdin=open(".idea/inputs/1244_input1.txt","r")

sw = int(input())
sw_list = list(map(int, input().split()))
number_students = int(input())

for _ in range(number_students):
    print(sw_list)
    s, idx = map(int,input().split())
    if s == 1: # man
        for sw_idx in range(idx, sw+1, idx):
            sw_list[sw_idx-1] = int(not sw_list[sw_idx-1])
        print("man:",sw_list)
    else:   #woman
        idx -= 1 # 인덱스에 접근을 쉽게하기위해
        cnt = 1
        sw_list[idx] = int(not sw_list[idx])  # 본인 인덱스는 무조건 바뀜
        while (0 <= idx - cnt) and (idx + cnt< sw): #
            print("sw_list[idx-cnt]:",sw_list[idx-cnt],"sw_list[idx+cnt]:",sw_list[idx+cnt])
            if sw_list[idx-cnt] == sw_list[idx+cnt]:
                sw_list[idx-cnt] = int(not sw_list[idx-cnt])
                sw_list[idx+cnt] = int(not sw_list[idx+cnt])
                cnt +=1
            else:
                break
        print("woman:",sw_list)

# 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다.
# 예를 들어 21번 스위치가 있다면 이 스위치의 상태는 둘째 줄 맨 앞에 출력한다.
# 켜진 스위치는 1, 꺼진 스위치는 0으로 표시하고, 스위치 상태 사이에 빈칸을 하나씩 둔다.
result = ''
for i in range(sw): #1~21
    result += str(sw_list[i])
    if i % 20 == 19:
        result += '\n'
    else:
        result += ' '
print(result)

