t = int(input())
number_list=[
    [10],       #0, 원래는 0이지만 출력할때 10이 나와야해서 고친다.
    [1],        #1   
    [2,4,8,6],  #2
    [3,9,7,1],  #3
    [4,6],      #4
    [5],        #5
    [6],        #6
    [7,9,3,1],  #7
    [8,4,2,6],  #8
    [9,1]       #9
    ]
for tc in range(t):
    result = 0
    a,b=map(int,input().split())
    len_list=len(number_list[a%10])
    print(number_list[a%10][(b-1)%len_list])
    

    