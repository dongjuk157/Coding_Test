expression = input()
num = ''
number = []
op = []
for ch in expression:
    if ch == '+' or ch == '-':
        op.append(ch)
        number.append(int(num))
        num = ''
    else:
        num += ch
else:
    number.append(int(num))

for i in range(1, len(number)):
    if op[i - 1] == '-' or number[i - 1] < 0:
        number[i] = -number[i]
print(sum(number))