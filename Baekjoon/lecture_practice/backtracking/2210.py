number_set = set()

matrix = [list(map(int, input().split())) for _ in range(5)]
delta = [(-1,0),(1,0),(0,-1),(0,1)]

def backtrack(x,y, index=0, string=''):
    if index == 5:
        number_set.add(string)
    else:
        for i in range(4):
            dx = x + delta[i][0]
            dy = y + delta[i][1]
            if 0 > dx or 5 <= dx or 0 > dy or 5 <= dy: continue
            backtrack(dx, dy, index+1, string+str(matrix[dx][dy]))

for i in range(5):
    for j in range(5):
        backtrack(i,j,0, str(matrix[i][j]))

print(len(number_set))