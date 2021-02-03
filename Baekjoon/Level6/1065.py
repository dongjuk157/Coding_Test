# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

def ishansu(str_number):
    # 한, 두자리 수인 경우 무조건 등차수열
    if len(str_number)== 1 or len(str_number)==2:
        return True

    # 세자리 수인 경우
    tmp = []
    for ch in str_number:
        tmp.append(int(ch))
    if (tmp[0]-tmp[1]) == (tmp[1]-tmp[2]):#  각 자리가 등차수열?
        return True
    else:
        return False

N = int(input())
result = 0
for i in range(1, N+1):
    if ishansu(str(i)):
        result += 1
print(result)
