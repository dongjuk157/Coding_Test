import sys; input = sys.stdin.readline
sys.setrecursionlimit(100000)
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

ind = [0] * (n + 1)
for i in range(len(inorder)):
    ind[inorder[i]] = i

def order(ins=0, ine=n - 1, pos=0, poe=n - 1):
    if ins > ine or pos > poe:
        return
    print(postorder[poe], end=' ')
    # ind = inorder.index(postorder[poe])
    l = ind[postorder[poe]] - ins
    r = ine - ind[postorder[poe]]

    order(ins, ins + l - 1, pos, pos + l - 1)
    order(ine - r + 1, ine, poe - r, poe - 1)
order()
