matrix = [[False] * 101 for _ in range(101)]
for i in range(4):
    bx, by, tx, ty = map(int, input().split())
    for r in range(by, ty):
        for c in range(bx, tx):
            if not matrix[r][c]:
                matrix[r][c]=True

result = 0
for i in range(100):
    result += sum(matrix[i])
print(result)