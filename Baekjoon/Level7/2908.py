tmp = ''.join([ch for ch in reversed(input())])
a, b = map(int,tmp.split())
print(a if a>b else b)

# 타인의 코드
# print(max(input()[::-1].split()))