n, m = map(int, input().split())

def asdf(index=0, end=n, key=m, arr=[]):
    if index == key:
        print(' '.join(map(str, arr)))
    else:
        for i in range(1, end+1):
            asdf(index=index+1, arr= arr+[i])


asdf()