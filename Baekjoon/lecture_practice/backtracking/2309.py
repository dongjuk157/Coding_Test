dwarf = [int(input()) for _ in range(9)]
#dwarf = [20, 7, 23, 19, 10, 15, 25, 8, 13]
visited = [0] * 9
real_dwarf = []

def backtrack(index, total, vis_idx, arr, visit):
    if index == 7 and total == 100:
        real_dwarf.append([dwarf[i] for i in range(9) if visit[i]])
        return
    elif index > 7 or total > 100:
        return
    else:
        for i in range(vis_idx + 1, 9):
            if visit[i] == 0:
                visit[i] = 1
                backtrack(index + 1, total + arr[i], i, arr, visit)
                visit[i] = 0


backtrack(0, 0, -1, dwarf, visited)
print('\n'.join(map(str, sorted(real_dwarf[0]))))