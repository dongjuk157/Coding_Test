import sys; input = sys.stdin.readline

def find_answer(word_list):
    ret = ''.join(word_list)
    for i in range(len(word_list) - 2, -1, -1): # 맨 앞뒤는 제거
        # 문자간 distance가 가장 작은 값 탐색
        min_dist = 32
        min_ind = -1
        for j in range(i + 1, len(word_list)):
            # 바뀌는 값이 같거나 이전 알파벳이면 넘어감
            if ord(word_list[i]) >= ord(word_list[j]): continue
            if ord(word_list[j]) - ord(word_list[i]) < min_dist:
                min_dist = ord(word_list[j]) - ord(word_list[i])
                min_ind = j
        if min_ind != -1:
            word_list[i], word_list[min_ind] = word_list[min_ind], word_list[i]
            lst = sorted(word_list[i + 1:])
            for j in range(i + 1, len(word_list)):
                word_list[j] = lst[j - i - 1]
            ret = ''.join(word_list)
            break
    return ret



def main():
    for _ in range(int(input())):
        print(find_answer(list(input().rstrip())))

if __name__ == '__main__':
    main()
