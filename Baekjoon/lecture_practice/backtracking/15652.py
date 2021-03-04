n, m = map(int, input().split())

def asdf(index=0, start=1,end=n, key=m, arr=[]):
    if index == key:
        print(' '.join(map(str, arr)))
    else:
        for i in range(start, end+1):
            asdf(index=index+1, start=i , arr= arr+[i])


asdf()