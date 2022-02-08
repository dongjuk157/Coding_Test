def main():
    k = int(input()) - 1
    answer = 0
    while k:
        answer += k & 1
        k >>= 1
    print(answer % 2)

if __name__ == "__main__":
    main()
