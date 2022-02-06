def main():
    n, m = map(int, input().split())
    fact = [1 for _ in range(n + 1)]
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i
    print(fact[n] // fact[n-m] // fact[m])


if __name__ == '__main__':
    main()
