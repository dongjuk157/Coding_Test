import sys
input = sys.stdin.readline

n,k = map(int,input().split())
num_list = list(map(int,input().split(',')))

while k > 0:
    tmp = list()
    for idx in range(n - 1):
        tmp.append(num_list[idx + 1] - num_list[idx])
    num_list = tmp
    n -= 1
    k -= 1
print(','.join(map(str,num_list)))
