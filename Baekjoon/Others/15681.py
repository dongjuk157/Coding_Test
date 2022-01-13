import sys; input = sys.stdin.readline
sys.setrecursionlimit = 10**9
linked_list = None
visit = None
# son_list = None
def postorder(cur_node):
    global linked_list, visit
    visit[cur_node] = 1
    num_of_son = 0
    for son in linked_list[cur_node]:
        if visit[son]: continue
        num_of_son += postorder(son)
    visit[cur_node] += num_of_son
    return visit[cur_node] # son + cur

def main():
    global linked_list, visit,son_list
    N, R, Q = map(int, input().split())
    linked_list = [[] for _ in range(N + 1)]
    visit = [0 for _ in range(N + 1)]
    # son_list = [0 for _ in range(N + 1)]
    for _ in range(N - 1):
        U, V = map(int, input().split())
        linked_list[U].append(V)
        linked_list[V].append(U)

    postorder(R)
    # print(visit)
    ans = ''
    for _ in range(Q):
        ans += str(visit[int(input())]) + '\n'
    print(ans)

if __name__ == "__main__":
    main()
