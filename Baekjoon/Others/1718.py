def main():
    p = input()
    k = input()
    answer = ''
    for i in range(len(p)):
        ch = p[i]
        if ch == ' ':
            answer += ch
            continue
        k_ch = k[i % len(k)]
        tmp = (ord(ch) - ord(k_ch) - 1) % 26
        answer += chr(97+tmp)
    print(answer)

if __name__ == '__main__':
    main()


