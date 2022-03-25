# import sys; input = sys.stdin.readline
from collections import defaultdict
def main():
    R, C, K = map(int, input().split())
    R -= 1
    C -= 1
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(3):
        for j, v in enumerate(map(int, input().split())):
            arr[i][j] = v
    # print(*arr, sep='\n')
    num_r, num_c = 3, 3
    answer = 0
    while arr[R][C] != K and answer <= 100:
        if num_r >= num_c:
            # R 연산
            for i in range(num_r): # 모든 행에 대해서 정렬 수행

                # 각각의 수가 몇 번 나왔는지 확인
                row_dict = defaultdict(int)
                for j in range(num_c):
                    row_dict[arr[i][j]] += 1
                # 0을 제외한 수 정렬
                sorted_dict = sorted(row_dict, key=lambda x: (row_dict[x], x))
                idx = 0
                for k in sorted_dict:
                    if k == 0: continue
                    arr[i][idx] = k
                    arr[i][idx + 1] = row_dict[k]
                    idx += 2
                    if idx >= 100:
                        break
                num_c = max(num_c, idx)
                for j in range(idx, num_c + 1):
                    arr[i][j] = 0
        else:
           # C연산
            for i in range(num_c):  # 모든 열에 대해서 정렬 수행
                # 각각의 수가 몇 번 나왔는지 확인
                col_dict = defaultdict(int)
                for j in range(num_r):
                    col_dict[arr[j][i]] += 1
                # 0을 제외한 수 정렬
                sorted_dict = sorted(col_dict, key=lambda x: (col_dict[x], x))
                idx = 0
                for k in sorted_dict:
                    if k == 0: continue
                    arr[idx][i] = k
                    arr[idx + 1][i] = col_dict[k]
                    idx += 2
                    if idx >= 100:
                        break
                num_r = max(num_r, idx)
                for j in range(idx, num_r + 1):
                    arr[j][i] = 0

        answer += 1
    # output
    if answer > 100:
        print(-1)
    else:
        print(answer)

if __name__ == "__main__":
    main()