import sys; input = sys.stdin.readline

N = int(input())
node_parent = [-1 for _ in range(N)]
node_son = [[] for _ in range(N)]
root = 0
for son, parent in enumerate(map(int, input().split())):
    if parent == -1:
        root = son
        continue
    node_son[parent].append(son)
removed_node = int(input())
answer = 0
def postorder(cur_node):
    if cur_node == removed_node:
        return
    if not len(node_son[cur_node]) or (len(node_son[cur_node]) == 1 and node_son[cur_node][0] == removed_node):
        global answer
        answer += 1
        return
    for son in node_son[cur_node]:
        postorder(son)

postorder(root)
print(answer)
