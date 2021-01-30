number = []
for _ in range(9):
    number.append(int(input()))

max_val = max(number)
ind_val = number.index(max_val) + 1
print(max_val, ind_val)