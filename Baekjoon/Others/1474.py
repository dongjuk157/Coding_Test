# import sys; input = sys.stdin.readline
def main():
    N, M = map(int, input().split())
    word_list = []
    total_length = 0
    for _ in range(N):
        tmp = input().rstrip()
        total_length += len(tmp)
        word_list.append(tmp)

    # print(word_list)
    # print((M - total_length) // (N - 1), (M - total_length) % (N - 1))
    answer = []
    underline = '_' * ((M - total_length) // (N - 1))
    remainder = (M - total_length) % (N - 1)
    for i in range(N - 1):
        answer.append(word_list[i])
        answer.append(underline)
        if remainder and word_list[i+1][0].islower():
            answer.append('_')
            remainder -= 1
    answer.append(word_list[-1])

    if remainder:
        for i in range(len(answer)-1, -1, -1):
            if remainder and answer[i][0].isupper():
                answer[i] = '_' + answer[i]
                remainder -= 1
    print(''.join(answer))


if __name__ == '__main__':
    main()
