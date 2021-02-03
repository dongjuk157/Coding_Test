# 숫자 다이얼 +1 초, 0 만 11초
#-> 1, 0 안눌림 2~9만 판단
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
        # 3s    4s    5s    6s    7s    8s     9s   10s
S= input()
result = 0
for ch in S:
    for idx,d in enumerate(dial):
        if ch in d:
            result += idx +3
            break
print(result)

