import sys; input = sys.stdin.readline
# 1 collections.Counter 사용
# from collections import Counter
# def main():
#     N = int(input())
#     c = Counter([input().rstrip() for _ in range(2 * N - 1)])
#     for k, v in c.items():
#         if v & 1:
#             print(k)
#             break

def main():
    N = int(input())
    s = set()
    for _ in range(2 * N - 1):
        tmp = input()
        if tmp in s:
            s.remove(tmp)
        else:
            s.add(tmp)
    print(s.pop())



if __name__ == '__main__':
    main()
