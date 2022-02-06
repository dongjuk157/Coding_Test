from math import isqrt
def findPrime(N):
    prime = [1 for _ in range(N + 1)]
    prime[0] = prime[1] = 0
    for i in range(2, isqrt(N) + 1):
        if prime[i]:
            for j in range(i + i, N + 1, i):
                prime[j] = 0
    return prime

def sanggn(n):
    visit = [0 for _ in range(100*7)]
    tmp = 0
    while 1:
        while n:
            tmp += (n % 10) ** 2
            n //= 10

        if tmp == 1:
            return True

        if visit[tmp]:
            return False
        visit[tmp] = 1
        n = tmp
        tmp = 0

def main():
    n = int(input())
    prime = findPrime(n)
    answer = []
    for i in range(2, n + 1):
        if prime[i] and sanggn(i):
            answer.append(i)

    print('\n'.join(map(str, answer)))


if __name__ == "__main__":
    main()
