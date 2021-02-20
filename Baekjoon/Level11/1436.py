six_list = []
cnt = 665
while len(six_list)<10000:
    if '666' in str(cnt):
        six_list.append(cnt)
    cnt += 1

n = int(input())
print(six_list[n-1])