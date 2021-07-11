i=input
for x in sorted([list(map(int,i().split())) for _ in range(int(i()))], key=lambda x:(x[1],x[0])):print(x[0],x[1])