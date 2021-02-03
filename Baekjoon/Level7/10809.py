s=input()
alpha = [-1]*(ord('z')-ord('a')+1)
#
#print(len(alpha))
#print(ord('z'))
#ord('a')~ ord('z')
# 0+97   ~ 25+97 = 122
for index, ch in enumerate(s):
    if alpha[ord(ch)-97] == -1:
        alpha[ord(ch)-97] = index
for n in alpha:
    print(n,end=' ')

# b 0
# a 1 
# e 2
# k 3
# j 4
# o 5
# o -
# n 7

## 타인의 코드
# string = str(input())
# alphbet = 'abcdefghijklmnopqrstuvwxyz'

# for i in alphbet: 
#   print(string.find(i), end = ' ')