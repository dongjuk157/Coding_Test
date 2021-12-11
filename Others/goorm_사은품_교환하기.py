for tc in range(1, 1 + int(input())):
	n, m = map(int, input().split())
	if n < 5:
		print(0)
	else:
		total = n + m 
		print(min(total//12, n//5))
		