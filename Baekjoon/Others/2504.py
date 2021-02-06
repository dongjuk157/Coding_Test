s=input()
stack=[]
result = 0
if s.count('(') != s.count(')') or s.count('[') != s.count(']'):
    s='' 

for ch in s:
    tmp = []
    if ch == ']': 
        while stack!=[]:
            tmp_ch = stack.pop()
            if tmp_ch == '[':
                break
            else:
                tmp.append(tmp_ch)
        if tmp == []:
            stack.append(3)
        else: #tmp !=[]
            for temp in tmp:
                if not isinstance(temp,int):
                    stack.append('_')
                    break
            else:
                stack.append(sum(tmp)*3)
    elif ch ==')':
        while stack!=[]:
            tmp_ch = stack.pop()
            if tmp_ch == '(':
                break
            else:
                tmp.append(tmp_ch)
        if tmp == []:
            stack.append(2)
        else: #tmp !=[]
            for temp in tmp:
                if not isinstance(temp,int):
                    stack.append('_')
                    break
            else:
                stack.append(sum(tmp)*2)
    else:
        stack.append(ch)
for i in stack:
    if isinstance(i, int):
        result += i
    else:
        result = 0
        break
print(result)
