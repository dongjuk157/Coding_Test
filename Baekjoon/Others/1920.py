import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()
M = int(input())
M_list = list(map(int, input().split()))
# M_list의 원소가 N_list에 존재하는지 알아내는 문제

def binarySearch(s, e, key):
    while s <= e:
        m = (s + e) // 2
        if N_list[m] == key:
            return 1
        elif N_list[m] < key:
            s = m + 1
        else: # N_list[m] > key
            e = m - 1
    return 0

for i in range(len(M_list)):
    print(binarySearch(0, N - 1, M_list[i]))
