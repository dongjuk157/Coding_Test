answer=''
while 1:
    a,b=map(int,input().split())
    if not (a or b): break
    m = a % b
    f = b % a
    if not m: answer += 'multiple\n'
    elif not f: answer += 'factor\n'
    else: answer += 'neither\n'
print(answer)