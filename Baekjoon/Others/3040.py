# import sys; input = sys.stdin.readline
from itertools import combinations
def main():
    dwarves = [int(input()) for _ in range(9)]
    total = sum(dwarves)
    rm_v1, rm_v2 = None, None
    for v1, v2 in combinations(dwarves, 2):
        if total - v1 - v2 == 100:
            rm_v1, rm_v2 = v1, v2
            break
    dwarves.remove(rm_v1)
    dwarves.remove(rm_v2)
    print(*dwarves, sep="\n")

if __name__ == '__main__':
    main()
