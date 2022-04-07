import sys; input = sys.stdin.readline

def is_palindrome(s):
    middle = len(s) // 2 + 1
    if s[:middle] == s[-middle:][::-1]:
        return True
    return False


def like_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[(len(s) - 1) - i]:
            if is_palindrome(s[:i] + s[i + 1:]) \
                    or is_palindrome(s[:len(s) - 1 - i] + s[len(s) - i:]):
                return True
            else:
                return False


def main():
    T = int(input())
    strings = [input().rstrip() for _ in range(T)]
    answer = []
    for s in strings:
        if is_palindrome(s):
            answer.append(0)
        elif like_palindrome(s):
            answer.append(1)
        else:
            answer.append(2)
    print(*answer, sep='\n')


if __name__ == "__main__":
    main()
