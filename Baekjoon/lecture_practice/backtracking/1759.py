L, C = map(int, input().split())
char = input().split()
char.sort()
# C개 중 L개를 선택하여 만든 조합
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
def comb(index=0, arr=[], limit=L):
    if index == limit:
        vowel = {'a','e','i','o','u'}
        vow, con = 0, 0
        for i in range(limit):
            if arr[i] in vowel:
                vow += 1
            else:
                con += 1
        if vow < 1 or con < 2: return
        print(''.join(arr))
    else:
        for i in range(index, C):
            if arr and ord(arr[-1]) >= ord(char[i]): continue
            comb(index+1, arr+[char[i]])
comb()