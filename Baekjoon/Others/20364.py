# import sys; input = sys.stdin.readline
def check_owned(x, owned):
    land = 0
    while x > 0:
        if owned[x]:
            land = x
        x >>= 1
    return land

N, Q = map(int, input().split())
owned = [False for _ in range(N + 1)]
for i in range(Q):
    x = int(input())

    owned_land = check_owned(x, owned)
    if not owned_land:
        owned[x] = True
    print(owned_land)
