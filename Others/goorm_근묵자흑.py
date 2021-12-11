# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from math import ceil
n, k = map(int, input().split())
n_list = list(map(int, input().split()))
index = n_list.index(1)

if index == 0 or index == n-1:
	result = int((n - 1) / (k - 1))
	print(result)
else:
# 1) 왼쪽에서 몇번 가야 1이 나오는지
# 2) 오른쪽에서 몇번 가야 1이 나오는지
	result = ceil(index / (k-1))
	tmp2 = ceil((n - result*(k-1) - 1)/(k-1))
	print(result + tmp2)

