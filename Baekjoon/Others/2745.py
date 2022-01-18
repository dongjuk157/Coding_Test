import sys
nums_dict = dict(zip(
    map(chr, range(ord('A'), ord('Z') + 1)),
    range(ord('A') - ord('A') + 10, ord('Z') - ord('A') + 11)
))
for i in range(10):
    nums_dict[str(i)] = i

def main():
    N, B = sys.stdin.readline().split()
    B = int(B)
    ans = 0
    for num_ch in N:
        ans *= B
        ans += nums_dict[num_ch]
    print(ans)

if __name__ == '__main__':
    main()