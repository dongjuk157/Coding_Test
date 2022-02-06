def main():
    l = int(input())
    a = input()
    modulo = 1234567891
    r = 31
    hash_r = [1 for _ in range(51)]
    for i in range(1, l):
        hash_r[i] = (r % modulo * hash_r[i - 1] % modulo) % modulo
    answer = 0
    for i in range(l):
        answer += (ord(a[i]) - 97 + 1) * hash_r[i]
        answer %= modulo
    print(answer)


if __name__ == '__main__':
    main()
