# N & M (12)
import sys; input = sys.stdin.readline
def backtrack(lst=None):
    global N, M, nums, visit, answer
    if lst is None:
        lst = []
    if len(lst) == M:
        answer.add(tuple([nums[i] for i in lst]))
        return

    for i in range(N):
        if lst and nums[lst[-1]] > nums[i]: continue
        lst.append(i)
        backtrack(lst)
        lst.pop()


def main():
    global N, M, nums, visit, answer
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    answer = set()
    visit = [False for _ in range(N)]
    backtrack()

    print('\n'.join(map(lambda t:' '.join(map(str, t)), sorted(answer))))

if __name__ == '__main__':
    main()