N = int(input())
files = []
for _ in range(N):
    tmp = []
    tmp.extend(input())
    files.append(tmp)
len_file = len(files[-1])
result = []
for j in range(len_file):
    tmp = set()
    for i in range(N):
        tmp.add(files[i].pop())
    if len(tmp)==1:
        result.append(tmp.pop())
    else:
        result.append('?')
print(''.join(reversed(result)))