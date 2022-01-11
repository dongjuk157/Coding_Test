import sys; input = sys.stdin.readline

def find_sibling(me, son, parent):
    p, grand_p = None, None
    if parent.get(me):
        p = parent[me]
    if parent.get(p):
        grand_p = parent[p]
    if grand_p:
        answer = 0
        for p_brother in son[grand_p]:
            if not son.get(p_brother): continue
            answer += len(son[p_brother])
        return answer - len(son[p])

    return 0


def main():
    while 1:
        N, K = map(int, input().split())
        if N == 0 and K == 0:
            break
        nums = list(map(int, input().split()))
        son, parent = {}, {}
        # parent[nums[0]] = None
        p = -1
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 != nums[i]:
                p += 1

            if not parent.get(nums[i]):
                parent[nums[i]] = 0
            parent[nums[i]] = nums[p]

            if not son.get(nums[p]):
                son[nums[p]] = set()
            son[nums[p]].add(nums[i])
        print(find_sibling(K, son, parent))

if __name__ == '__main__':
    main()
