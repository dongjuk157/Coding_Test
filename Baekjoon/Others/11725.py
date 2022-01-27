import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def order(adj_list, cur_node=1):
    global parent
    if cur_node != 1 and len(adj_list[cur_node]) == 1:
        return

    for son in adj_list[cur_node]:
        if son == parent[cur_node]: continue
        parent[son] = cur_node
        order(adj_list, son)

def main():
    global parent
    N = int(input())
    adj_list = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    parent = [0 for _ in range(N + 1)]
    order(adj_list)

    print(*[v for i, v in enumerate(parent) if i > 1], sep='\n')

if __name__ == "__main__":
    main()
