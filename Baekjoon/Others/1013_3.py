import sys; input = sys.stdin.readline

def string_check(s):
    # p = re.compile('(100+1+|01)+')
    i = 0
    while i < len(s):
        # 1 100+1+
        if s[i] == '1' and i + 1 < len(s) and s[i + 1] == '0': # 1-0 '10'
            i += 2
            if i < len(s) and s[i] == '0':          # 1-1 '100'
                i += 1
                while i < len(s) and s[i] == '0':   # 1-2 '100+'
                    i += 1
            else:
                return False
            if i < len(s) and s[i] == '1':          # 1-3 100+1
                i += 1
                while i < len(s) and s[i] == '1':   # 1-4 100+1+
                    i += 1
            else:
                return False

            if i == len(s):
                return True
        # 2 01
        elif s[i] == '0' and i + 1 < len(s) and s[i + 1] == '1':
            i += 2
        # 3 00 => 10011001 => 10011/001인 상태이므로 이전 인덱스 두개 확인
        elif s[i] == '0' and i + 1 < len(s) and s[i + 1] == '0':
            if i - 1 >= 0 and s[i - 1] == '1' and i - 2 >= 0 and s[i-2] == '1':
                i -= 1
            else:
                return False
        else: # '11'
            return False
    return True


def main():
    T = int(input())
    for _ in range(T):
        s = input().rstrip()
        print("YES" if string_check(s) else "NO")

if __name__ == "__main__":
    main()