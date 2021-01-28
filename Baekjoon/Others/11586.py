N = int(input())
mirror = []
for i in range(N):
    mirror.append(input())
mirror_simri = int(input())

if mirror_simri == 1:   # 1: 원본
    for mr in mirror:
        print(mr)
elif mirror_simri == 2: # 2: 좌우 반전
    for mr in mirror:
        print(mr[::-1])
elif mirror_simri == 3: # 3: 상하 반전
    for mr in reversed(mirror):
        print(mr)


# if mirror_simri == 1:     # 1 원본
#     for mr in mirror:
#         print(''.join(mr))
# elif mirror_simri == 2:   # 2 좌우반전
#     for mr in mirror:
#         print(''.join(mr[::-1]))
# elif mirror_simri == 3:   # 3 상하좌우 반전 <- C
#     for i in range(N):
#         for j in range(N):
#             print(mirror[7-i][7-j])