fact_mod = None
M = 1_000_000_007

def pow_mod(number, k):
    if 0 == k:
        return 1
    x = pow_mod(number, k >> 1)
    if k & 1:   # odd
        return (x * x * number) % M
    else:       # even
        return (x * x) % M

def find_binomial_coefficient(N, K):
    nfacto = fact_mod[N]
    nkfacto = fact_mod[N - K]
    kfacto = fact_mod[K]
    reverse_val = pow_mod(nkfacto * kfacto % M, M - 2)
    ret = (nfacto * reverse_val) % M
    return ret

def main():
    N, K = map(int, input().split())
    global fact_mod
    fact_mod = [1 for _ in range(N + 1)]
    for i in range(2, N + 1):
        fact_mod[i] = (fact_mod[i - 1] * i) % M
    print(find_binomial_coefficient(N, K))

if __name__ == "__main__":
    main()
