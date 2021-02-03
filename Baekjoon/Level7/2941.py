s =input()
result = 0
alpha2=['c=','c-','dz=','d-','lj','nj','s=','z=']
index=0
while s != '__':
    tmp = s.find(alpha2[index])
    if tmp == -1:
        if index == 7:
            break
        index += 1
    else:
        s = s.replace(alpha2[index],'_',1)
        result += 1        

for ch in s:
    if ch != '_':
        result += 1
print(result)
    

# 1 이방법으로 하면 nljj에서 lj를 빼고 nj가 남게됨.

# 타인의 코드
a = input()
b = ['c=','c-','z=','d-','lj','nj','s=','dz=']
tmp = len(a)
for i in b:
    tmp -= a.count(i)
print(tmp)
