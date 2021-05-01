import sys; i = sys.stdin.readline
N, M = map(int, i().split())
d = set([i().rstrip() for _ in range(N)])
b = set([i().rstrip() for _ in range(M)])
db = sorted(list(d & b))
print(len(db), *db, sep='\n')

