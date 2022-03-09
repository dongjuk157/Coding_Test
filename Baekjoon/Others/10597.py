# import sys; input = sys.stdin.readline
def backtrack(ind, limit):
    global s, stack
    if ind == limit:
        max_v = max(stack)
        for i in range(1, max_v+1):
            if visit[i] != 1:
                return
        print(*stack)
        exit(0)
        # return
    tmp = int(s[ind])
    if not visit[tmp]:
        visit[tmp] = 1
        stack.append(tmp)
        backtrack(ind + 1, limit)
        visit[tmp] = 0
        stack.pop()

    if ind + 2 > limit: return
    tmp = int(s[ind:ind+2])
    if tmp <= 50 and not visit[tmp]:
        visit[tmp] = 1
        stack.append(tmp)
        backtrack(ind + 2, limit)
        visit[tmp] = 0
        stack.pop()


def main():
    global s, stack, visit
    visit = [0 for _ in range(51)]
    s = input().rstrip()
    stack = []
    backtrack(0, len(s))


if __name__ == "__main__":
    main()
