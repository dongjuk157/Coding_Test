while True:
    k, *S = map(int, input().split())
    if k == 0: break
    visited = [0] * k


    def lotto(index=0, arr=[]):
        if index == 6:
            print(*arr)
            return
        else:
            for i in range(index, k):
                if visited[i] == 0:
                    if arr and arr[-1] > S[i]: continue # 오름차순
                    visited[i] = 1
                    lotto(index + 1, arr + [S[i]])
                    visited[i] = 0
    lotto()
    print()

