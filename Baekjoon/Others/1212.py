n = input()
#n = '7'*333333
oc_dict= {'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101','6':'110','7':'111',}
n_decimal = 0
result = ''
for idx in range(len(n)):
    if idx == 0:
        result += str(int(oc_dict[n[idx]]))
    else:
        result += oc_dict[n[idx]]
print(result)