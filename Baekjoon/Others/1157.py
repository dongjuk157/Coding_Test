#알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.
#첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
#  주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
#  단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

string = input().upper() # 알파벳을 대소문자 구분 안하는데, 대문자로 출력해야됨
alpha = dict()
for ch in string:
    if not ch in alpha:
        alpha[ch] = 0
    alpha[ch] += 1

alpha = sorted(alpha.items(), key=lambda x:x[1])
max_ch,max_val = alpha.pop()
if alpha==[]:
    print(max_ch)
elif max_val == (alpha.pop())[1]:
    print("?")
else:
    print(max_ch)

# # 타인의 코드 1
# word = input().upper()
# S = list(set(word))
# cnt = []

# for v in S:
#     cnt.append(word.count(v))

# if cnt.count(max(cnt))>=2:
#     print('?')
# else:
#     print(S[(cnt.index(max(cnt)))])

# # 타인의 코드 2
# s = input().upper()

# a = []
# for i in range(65, 91):
#     a.append(int(s.count(chr(i))))
# if (a.count(max(a)) > 1):
#     print("?")
# else:
#     print(chr(a.index(max(a)) + 65))
