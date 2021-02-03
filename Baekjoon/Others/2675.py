t = int(input())
for _ in range(t):
    r,s = map(str,input().split())
    for ch in s:
        print(ch*int(r),end='')
    print()