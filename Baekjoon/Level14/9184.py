dp_w = [[[1] * 101 for i in range(101)] for j in range(101)]
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i <= 0 or j <= 0 or k <= 0:
                dp_w[i][j][k] = 1
            elif i < j < k:
                dp_w[i][j][k] = dp_w[i][j][k - 1] + dp_w[i][j - 1][k - 1] - dp_w[i][j - 1][k]
            else:
                dp_w[i][j][k] = dp_w[i - 1][j][k] + dp_w[i - 1][j - 1][k] + dp_w[i - 1][j][k - 1] - dp_w[i - 1][j - 1][
                    k - 1]
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return dp_w[20][20][20] #dp_w[a][b][c] = dp_w[20][20][20]
    else:
        return dp_w[a][b][c]

while True:
    x, y, z = map(int, input().split())

    if x == -1 and y == -1 and z== -1:
        break
    print("w({}, {}, {}) = {}".format(x, y, z, w(x, y, z)))
