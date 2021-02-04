n,m=map(str,input().split())
n='0b'+n
m='0b'+m
result = int(n,2)+int(m,2)
print(bin(result)[2:])