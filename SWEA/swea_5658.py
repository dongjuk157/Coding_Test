def find_number(string, string_size, split_size, order):
    # string: modify string
    # string_size: real string length
    # split size
    ret = set()
    for i in range(split_size):
        for j in range(i, i + string_size, split_size):
            ret.add(int(string[j:j + split_size], 16))
    ret = sorted(ret)
    ret = ret[len(ret) - order]

    return ret

def main():
    T = int(input())
    for tc in range(1, T + 1):
        # 0 initiate
        N, K = map(int, input().split())
        s = input().rstrip()
        s += s[:N//4]

        answer = find_number(s, N, N//4, K)
        # 2 output
        print(f"#{tc} {answer}")


if __name__ == "__main__":
    main()
