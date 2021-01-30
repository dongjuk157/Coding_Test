# 자기점수중 최대값 M
# 모든점수 = 점수 / M * 100

N = int(input())
scores = list(map(int,input().split()))
max_score = max(scores)

print( (sum(scores)/max_score * 100) / N)
