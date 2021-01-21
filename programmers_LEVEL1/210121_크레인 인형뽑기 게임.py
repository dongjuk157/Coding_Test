def solution(board, moves):
    answer = 0 #사라진 갯수
    board2=[]
    barguni =[]
    
    for i in range(len(board)): 
        tmp=[]
        for j in range(len(board)):
            if board[j][i]!=0:
                tmp.append(board[j][i]) 
        tmp.reverse()
        board2.append(tmp)
    
    # moves: 위치 배열
    for mv in moves:
        if board2[mv-1] !=[]:
            barguni.append(board2[mv-1].pop())
        if len(barguni)>=2:
            if barguni[-1] == barguni[-2]:
                barguni.pop()
                barguni.pop()
                answer+=2

    return answer

################################
def solution(board, moves):
    stack = []
    result = 0
    for move in moves:
        for row in board:
            if row[move-1]:
                stack.append(row[move-1])
                row[move-1] = 0
                break
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            result += 2
    return result