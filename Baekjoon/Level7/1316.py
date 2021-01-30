n = int(input())

result=0
for case in range(n):
    word = input()
    chk_char = ''
    for ch in word:		
        if ch not in chk_char:     # chk에 없으면 추가
            chk_char += ch
        else:		                # 있는경우에는 
            if ch != chk_char[-1]: # 이전값이랑 비교해서 다르면 멈춤
                break
    else:	# 문제 없이 끝나면 +1
        result += 1

print(result)