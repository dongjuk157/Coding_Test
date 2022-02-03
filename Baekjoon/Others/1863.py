import sys; input = sys.stdin.readline

def main():
    N = int(input())
    building = [0]
    answer = 0
    for _ in range(N):
        x, cur_h = map(int, input().split())

        if cur_h > building[-1]:
            answer += 1
            building.append(cur_h)
        else: # cur_h < building[-1]
            while building[-1] > cur_h:
                building.pop()

            if building[-1] < cur_h:
                answer += 1
                building.append(cur_h)
    print(answer)


if __name__ == '__main__':
    main()
