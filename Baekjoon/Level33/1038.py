desc_nums = []
visit = [False for _ in range(10)]
def make_number(visit):
    ret = 0
    for i in range(9, -1, -1):
        if visit[i]:
            ret = ret * 10 + i
    return ret

def backtrack(ind=-1, prev=-1):
    if ind == 10:
        return

    for i in range(ind + 1, 10):
        if prev >= i: continue
        if visit[i]: continue
        visit[i] = True
        desc_nums.append(make_number(visit))
        backtrack(i)
        visit[i] = False

def main():
    N = int(input())
    backtrack()
    desc_nums.sort()
    if N < len(desc_nums):
        print(desc_nums[N])
    else:
        print(-1)

if __name__ == "__main__":
    main()