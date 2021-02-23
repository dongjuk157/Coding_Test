import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medal = list()
k_medal = tuple()
for _ in range(n):
    tmp = tuple(map(int, input().split()))
    if tmp[0] == k:
        k_medal = tmp
    else:
        medal.append(tmp)
print(medal,k_medal)
up = []
for md in medal:
    if md[1] == k_medal[1]:
        if md[2] == k_medal[2]:
            if md[3] > k_medal[3]:
                up.append(md)
        elif md[2] > k_medal[2]:
            up.append(md)
    elif md[1] > k_medal[1]:
        up.append(md)
print(up)
print(len(up)+1)

