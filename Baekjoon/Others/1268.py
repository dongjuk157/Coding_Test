# N = int(input())
# list_2 = []
# for _ in range(N):
#     list_2.append(list(map(int,input().split())))
list_2= [[2, 3, 1, 7, 3], [4, 1, 9, 6, 8], [5, 5, 2, 6, 4], [6, 5, 2, 6, 7], [8, 4, 2, 2, 2],[5, 5, 2, 4, 4]]
N=len(list_2)


student=[] # 학생별로 겹치는 학생을 저장
for i in range(N):
    student.append(set())

tmp1=[]     # i,j => j,i
for i in range(5):
    tmp2 = []
    for j in range(N):
        tmp2.append(list_2[j][i])
    tmp1.append(tmp2)        

for i, list_1 in enumerate(tmp1):       # 자신을 포함하여 겹치는 반인 경우 student에 저장
    for j, val1 in enumerate(list_1):
        for k, val2 in enumerate(list_1):
            if val1 == val2:
                student[j].add(k)
#print(student)
# tmp = []
# for idx, std in enumerate(student):     # 막무가내로 넣었으니까 중복 제거
#     tmp.append((idx+1,len(set(std))))
max_idx, max_val = 0,0
for idx, val in enumerate(student):
    len_val = len(val)
    if len_val>max_val:
        max_idx = idx+1
        max_val = len_val
print(max_idx)
# tmp.sort(key=lambda x: x[1], reverse=True)  # 정렬해서 가장 큰값 찾고
# print(tmp[0][0])                            # 그때 인덱스 출력