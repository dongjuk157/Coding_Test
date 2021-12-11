import sys
sys.stdin=open('.idea/inputs/1063_input1.txt','r')

move_delta = {
    'R' : (0, 1),
    'L' : (0, -1),
    'B' : (-1, 0),
    'T' : (1, 0),
}

matrix = [[0]*8 for i in range(8)]
king, stone, n = input().split()
for _ in range(int(n)):
    move = input()
    tmp_move = [0, 0]
    for movement in move:
        tmp_move[0] += move_delta[movement][0] #r
        tmp_move[1] += move_delta[movement][1] #c
    print(move, tmp_move)
    if ord('A') <= ord(king[0])+tmp_move[1] <= ord('H') and 1 <= int(king[1])+tmp_move[0] <= 8:
        if stone == chr(ord(king[0]) + tmp_move[1])+str(int(king[1])+tmp_move[0]):
            if ord('A') <= ord(stone[0])+tmp_move[1] <= ord('H') and 1 <= int(stone[1])+tmp_move[0] <= 8:
                king = chr(ord(king[0]) + tmp_move[1]) + str(int(king[1]) + tmp_move[0])
                stone = chr(ord(stone[0]) + tmp_move[1]) + str(int(stone[1]) + tmp_move[0])
        else:
            king = chr(ord(king[0]) + tmp_move[1]) + str(int(king[1]) + tmp_move[0])
    print(king,stone)

print(king)
print(stone)