from collections import deque
N= int(input())
cards = deque(range(1,N+1))
#1,~,N -> 2,~,N => 3,~,N,2
while len(cards) != 1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])