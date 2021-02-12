import sys
input = sys.stdin.readline
t = int(input())

for tc in range(t):
    K=int(input())
    N=int(input())
    floor =[[i for i in range(1,15)]]
    for k in range(1,K+1):
        tmp= []
        for n in range(N):
            tmp.append(sum(floor[k-1][:n+1]))
        floor.append(tmp)
    #print(floor)
    print(floor[K][N-1])
    
    # k층, n호 
    # 3층 1호 1명   3층 2호 5   3층 3호 16
    # 2층 1호 1명   2층 2호 4   2층 3호 10      => 
    # 1층 1호 1명   1층 2호 3   1층 3호 6.  i호 =>sum(range(i+1))
    # 0층 1호 1명   0층 2호 2   0층 3호 3.  i호 => i명

#  1  2  3  4  5  6  7  8  9 10  => i
#  1  3  6 10 15 21 28 36 45 55  => sum(floor[0][:n+1])
#  1  4 10 20 35 56 84 ...       => sum(floor[1][:n+1])