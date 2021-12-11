import sys; input = sys.stdin.readline

def backtrack(start=0, ind=0, total=0, bit=0):
    if answer:
        return
    if total > 100:
        return
    if ind == 7:
        if total == 100:
            for i in range(9):
                if bit & (1 << i):
                    answer.append(dwarf[i])
        return
    for i in range(start, 9):
        backtrack(i + 1, ind + 1, total + dwarf[i], bit | (1 << i))


dwarf = [int(input()) for _ in range(9)]
answer = []
backtrack()
print(*sorted(answer), sep='\n')