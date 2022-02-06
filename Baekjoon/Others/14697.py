def main():
    *room, total = map(int, input().split())
    for i in range((total // room[0]) + 1):
        tmp1 = room[0] * i
        for j in range((total // room[1]) + 1):
            tmp2 = room[1] * j
            for k in range((total // room[2]) + 1):
                tmp3 = room[2] * k
                if total == tmp1 + tmp2 + tmp3:
                    print(1)
                    return
    print(0)

if __name__ == "__main__":
    main()
