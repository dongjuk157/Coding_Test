import sys
input=sys.stdin.readline

n=int(input())
lst=[0,0,1,1,]
if n<=3:
    print(lst[n])
else:
    for num in range(4,n+1):
      if not num % 6:
          tmp = min(lst[num//3], lst[num//2], lst[num-1])+1
          lst.append(tmp)
      elif not num % 3:
          tmp = min(lst[num//3], lst[num-1])+1
          lst.append(tmp)
      elif not num % 2:
          tmp = min(lst[num//2], lst[num-1])+1
          lst.append(tmp)
      else:
          lst.append(lst[-1]+1)     
    print(lst[n])