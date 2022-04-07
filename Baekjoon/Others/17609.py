# import sys; input = sys.stdin.readline
def check_palindrome(string, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(string) - 1

    cnt = 0
    pre_idx, post_idx = start, end
    while pre_idx <= end and post_idx >= start:
        if pre_idx == (start + end + 1) // 2 \
                or post_idx == end - ((start + end + 1) // 2):
            if string[pre_idx] != string[post_idx]:
                cnt += 1
            break
        if cnt > 1:
            break

        if string[pre_idx] == string[post_idx]:
            pre_idx += 1
            post_idx -= 1
            continue

        cnt += 1
        if string[pre_idx + 1] == string[post_idx] and string[pre_idx] == string[post_idx - 1]:
            tmp1 = check_palindrome(string, pre_idx + 1, post_idx)
            tmp2 = check_palindrome(string, pre_idx, post_idx - 1)
            if not tmp1 or not tmp2:
                break
            else:
                continue

        elif string[pre_idx + 1] == string[post_idx]:
            pre_idx += 1
        elif string[pre_idx] == string[post_idx - 1]:
            post_idx -= 1
        else:
            return 2

    return cnt

def main():
    answer = []
    for _ in range(int(input())):
        answer.append(check_palindrome(input().rstrip()))
    print(*answer, sep='\n')


if __name__ == "__main__":
    main()
