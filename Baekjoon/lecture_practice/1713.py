import sys
input = sys.stdin.readline

n = int(input()) # photo
r = int(input()) # total recommend, r <= 1000
r_list = list(map(int, input().split()))

r_dict = dict()
photo = []
for recommend in r_list:
    if len(photo) < n:
        if recommend not in r_dict:
            r_dict[recommend] = 1
            photo.append(recommend)
        else:
            r_dict[recommend] += 1

    else:
        if recommend in photo:
            r_dict[recommend] += 1
        else:
            min_tmp = min([r_dict[photo[idx]] for idx in range(n)])
            for idx, pht in enumerate(photo):
                if r_dict[pht] == min_tmp:
                    r_dict[pht] = 0
                    photo.pop(idx)
                    break
            photo.append(recommend)
            if recommend not in r_dict:
                r_dict[recommend] = 1
            else:
                r_dict[recommend] += 1

print(' '.join(map(str, sorted(photo))))