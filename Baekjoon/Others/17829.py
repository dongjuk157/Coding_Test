# import sys; input = sys.stdin.readline

def second_max(r, c, arr):
    s = [arr[r][c], arr[r][c + 1], arr[r + 1][c], arr[r + 1][c + 1]]
    s.sort()
    s.pop()
    return s.pop()

def create_arr(arr):
    size = len(arr) // 2
    new_arr = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            new_arr[i][j]= second_max(2 * i, 2 * j, arr)
    return new_arr

def main():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    while len(arr) != 1:
        arr = create_arr(arr)
    print(arr[0][0])

if __name__ == '__main__':
    # main()
    import random
    with open('17829.txt', 'w') as f:
        N = 1024
        f.write(str(N))
        f.write('\n')
        for i in range(N):
            for j in range(N):
                f.write(str(int(random.random() * 20000) - 10000))
                f.write(' ')
            f.write('\n')

