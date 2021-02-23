print(' '.join(map(str,sorted([(i+1, sum(map(int,input().split()))) for i in range(5)], key=lambda x:x[1])[-1])))

l=[sum(map(int, input().split())) for _ in range(5)];print(l.index(max(l))+1,max(l))

