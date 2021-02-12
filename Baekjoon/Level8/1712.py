a,b,c = map(int,input().split())

if c-b<=0:
    print(-1)
else:
    print(a//(c-b) + 1)


# a,b,c = 1000,70,170
# a+b*n <= c*n
# a <= (c-b)*n
# a/(c-b) <= *n