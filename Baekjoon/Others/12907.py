N = int(input())
ans_list = list(map(int, input().split()))
ans_dict = dict(zip(range(41),[0] * 41))

for i in range(N):
    index = ans_list[i]
    ans_dict[index] += 1

len1 = 0
for i in range(41):
    if ans_dict[i] == 0:
        len1 = i
        break
    else:
        ans_dict[i] -= 1

len2 = 0
for i in range(41):
    if ans_dict[i] == 0:
        len2 = i
        break
    else:
        ans_dict[i] -= 1

break_chk = False
for i in range(41):
    if ans_dict[i]:
        break_chk = True
        break

if break_chk:
    print(0)
elif len1 == len2:
    print(1 << (len2))
else:
    print(1 << (len2 + 1))

