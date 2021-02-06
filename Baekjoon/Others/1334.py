s_num = input()

len_num=len(s_num)
s_num_half= s_num[:(len_num+1)//2]

result= ''

if s_num == '9'*len_num:
    print(int(s_num)+2)
elif len_num == 1:
    print(int(s_num)+1)

elif len_num%2:   # odd
    tmp = s_num_half + s_num_half[-2::-1]
    if int(tmp)> int(s_num):
        print(tmp)
    else:
        tmp = str(int(s_num_half)+1)
        tmp = tmp[:]+tmp[-2::-1]
        print(tmp)

else:           # even
    tmp = s_num_half[:] + s_num_half[::-1]
    if int(tmp)> int(s_num):
        print(tmp)
    else:
        tmp = str(int(s_num_half)+1)
        tmp = tmp[:]+tmp[::-1]
        print(tmp)
    