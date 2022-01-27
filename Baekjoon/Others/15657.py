# N & M (8)
import sys; input = sys.stdin.readline
def backtrack(lst=None, prev=0):
    global N, M, nums
    if lst is None:
        lst = []
    if len(lst) == M:
        print(*[nums[i] for i in lst])
        return

    for i in range(prev, N):
        lst.append(i)
        backtrack(lst, i)
        lst.pop()


def main():
    global N, M, nums
    N, M = map(int, input().split())
    nums = sorted(map(int, input().split()))
    backtrack()

if __name__ == '__main__':
    main()
