n, m = map(int, input().split())
visited = [0] * (n + 1)

def asdf(index=0, arr=[], key=m, end=n):
    if index == key:
        print(' '.join(map(str, arr)))
    else:
        for i in range(1,end+1):
            if visited[i] == 0:
                visited[i] = 1
                asdf(index + 1, arr + [i])
                visited[i] = 0

asdf()
