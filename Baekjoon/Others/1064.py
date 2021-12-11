xa, ya, xb, yb, xc, yc = map(int,input().split())
dx=[(xa-xb),(xb-xc),(xc-xa)]
dy=[(ya-yb),(yb-yc),(yc-ya)]
dist = [
    (dx[0] ** 2 + dy[0] ** 2) ** 0.5,
    (dx[1] ** 2 + dy[1] ** 2) ** 0.5,
    (dx[2] ** 2 + dy[2] ** 2) ** 0.5,
]

if dx[0]*dy[1] == dx[1]*dy[0] and dx[1]*dy[2] == dx[2]*dy[1] and dx[2]*dy[0] == dx[0]*dy[2]:
    same_grad = True
else:
    same_grad = False

if same_grad:
    print(-1.0)
else:
    result = 2 * (max(dist) - min(dist))
    print(f"{result:.15f}")
