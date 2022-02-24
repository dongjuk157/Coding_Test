def backtrack(ind, limit, prev):
    global nums, answer, visit
    if ind == limit:
        tmp = tuple([nums[i] for i, v in enumerate(visit) if v])
        if tmp not in answer:
            print(*tmp)
            answer.add(tmp)
        return
    for i in range(prev + 1, len(nums)):
        if visit[i]: continue
        visit[i] = 1
        backtrack(ind+1, limit, i)
        visit[i] = 0
        

def main():
    global nums, answer, visit
    N, M = map(int, input().split())
    nums = sorted(map(int, input().split()))
    answer = set()
    visit = [0 for _ in range(N)]
    backtrack(0, M, -1)


if __name__=="__main__":
    main()

