n = int(input())
save = set()
for i in range(n):
    tmp = input()
    save.add((len(tmp),tmp))

_list=sorted(save,key=lambda x: (x[0],x[1]))


for word in _list:
    print(word[1])

    