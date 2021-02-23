sum_list = []
sum_tmp = 0
result = 0
for _ in range(10):
    sum_tmp += int(input())
    sum_list.append(tuple([sum_tmp, abs(sum_tmp - 100)]))
sum_list.sort(key=lambda x:x[1])
if sum_list[0][1] == sum_list[1][1]:
    result = sum_list[1][0]
else:
    result = sum_list[0][0]
print(result)