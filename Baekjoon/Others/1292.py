a,b = map(int,input().split())

sum_list=[]
cnt=0
while len(sum_list)<=b:
    cnt += 1
    sum_list.extend([cnt]*cnt)

print(sum(sum_list[a-1:b]))
