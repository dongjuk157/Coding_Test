import sys; input = sys.stdin.readline
N, M, K = None, None, None
answer = -50_000
numbers = []
def adj_chk(index_num, index_list):
    global N, M
    for i in range(len(index_list)):
        if index_list[i] == index_num:
            return True
        r, c = index_list[i]//M, index_list[i] % M
        num_r, num_c = index_num //M, index_num % M
        if abs(num_c - c) == 0 and abs(num_r - r) == 1:
            return True
        if abs(num_r - r) == 0 and abs(num_c - c) == 1:
            return True
    return False

def backtrack(ind, total, prev=None):
    global N, M, K, answer
    if ind == K:
        answer = max(answer, total)
        return
    if not prev:
        prev = []
        s = 0
    else:
        s = prev[-1]
    for i in range(s, N * M):
        if adj_chk(i, prev): continue
        backtrack(ind+1, total+numbers[i], prev + [i])

def main():
    global N, M, K, answer
    N, M, K = map(int, input().split())
    for _ in range(N):
        numbers.extend(map(int, input().split()))
    backtrack(0, 0)
    print(answer)

if __name__ == '__main__':
    main()
