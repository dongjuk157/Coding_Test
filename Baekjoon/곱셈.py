num1= int(input())
num2=input()[::-1]
answer=[]

for i in num2:
    tmp=int(i)*num1
    answer.append(tmp)
    print(tmp)

print(answer[0]+answer[1]*10+answer[2]*100)