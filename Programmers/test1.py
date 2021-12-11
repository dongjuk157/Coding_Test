numbers = [2,7]
for i in range(len(numbers)):
    length = len(bin(numbers[i]))-2
    visit = [0] * (length)
    def backtrack(binary_length, ind=0, choice=[] ): # 조합 백트래킹
        n
        if ind == 2:
            return
        for i in range(ind, binary_length):
            if visit[i]: continue
            visit[i] = 1
            backtrack(binary_length, ind + 1, choice+[i])
            visit[i] = 0
    backtrack(length, 2)


