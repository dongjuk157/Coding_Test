# N & M (5)
import sys; input = sys.stdin.readline
def backtrack(ind, limit, size, nums, visit, lst=None):
    if lst is None:
        lst = []
    if ind == limit:
        print(*[nums[i] for i in lst])
        return

    for i in range(size):
        if visit[i]: continue
        visit[i] = True
        lst.append(i)
        backtrack(ind + 1, limit, size, nums, visit, lst)
        lst.pop()
        visit[i] = False


def main():
    N, M = map(int, input().split())
    nums = sorted(map(int, input().split()))
    visit = [False for _ in range(N)]
    backtrack(0, M, N, nums, visit)

if __name__ == '__main__':
    main()
