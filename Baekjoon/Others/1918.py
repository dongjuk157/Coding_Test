import sys; input = sys.stdin.readline
ans = ''
s = []
for ch in input().rstrip():
    if ch == '+' or ch == '-':
        while s:
            if s[-1] == '(':
                break
            ans += s.pop()
        s.append(ch)
    elif ch == '*' or ch == '/':
        while s:
            if s[-1] == '(' or s[-1] == '+' or s[-1] == '-':
                break
            ans += s.pop()
        s.append(ch)
    elif  ch == '(':
        s.append(ch)
    elif ch == ')':
        while s:
            tmp = s.pop()
            if tmp == '(':
                break
            ans += tmp
    else:
        ans += ch
else:
    while s:
        ans += s.pop()
print(ans)