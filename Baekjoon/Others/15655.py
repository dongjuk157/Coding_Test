# import sys;input = sys.stdin.readline
def backtrack(ind=0, cnt=0):
    global n, m, nums, ans_set, visit
    if cnt == m:
        tmp = tuple([nums[i] for i, v in enumerate(visit) if v])
        if tmp not in ans_set:
            ans_set.add(tmp)
            print(*tmp)
        return
    if ind == n:
        return
    if not visit[ind]:
        visit[ind] = 1
        backtrack(ind + 1, cnt + 1)
        visit[ind] = 0
    backtrack(ind + 1, cnt)

def main():
    global n, m, nums, ans_set, visit
    n, m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    ans_set = set()
    visit = [0 for _ in range(n)]
    backtrack()

if __name__ == "__main__":
    main()
