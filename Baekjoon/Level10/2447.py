def star_fuc(star_list):
    new_star_list = []
    for i in range(3 * len(star_list)):
        if i // len(star_list) == 1:
            new_star_list.append(star_list[i % len(star_list)] + ' ' * len(star_list) + star_list[i % len(star_list)])
        else:
            new_star_list.append(star_list[i % len(star_list)] * 3)

    return list(new_star_list)

star = ['***', '* *', '***']
n = int(input())
num = 0
while n != 3:
    n = int(n / 3)
    num = num + 1

for i in range(num):
    star = star_fuc(star)
for i in star:
    print(i)