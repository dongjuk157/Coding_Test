n = int(input())
n_list = list(map(int, input().split()))
operator = list(map(int, input().split()))
min_val = 1000000000
max_val = -1000000000
def backtrack(index, number=n_list[0]):
    if index == n - 1:
        global min_val, max_val
        if min_val > number:
            min_val = number
        if max_val < number:
            max_val = number
        return
    else:
        if operator[0]:
            operator[0] -= 1
            backtrack(index + 1, number + n_list[index + 1])
            operator[0] += 1
        if operator[1]:
            operator[1] -= 1
            backtrack(index + 1, number - n_list[index + 1])
            operator[1] += 1
        if operator[2]:
            operator[2] -= 1
            backtrack(index + 1, number * n_list[index + 1])
            operator[2] += 1
        if operator[3] and n_list[index + 1]:
            operator[3] -= 1
            backtrack(index + 1, int(number / n_list[index + 1]))
            operator[3] += 1

backtrack(0)
print(max_val, min_val, sep='\n')