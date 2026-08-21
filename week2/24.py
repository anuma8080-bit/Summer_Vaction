r,c = map(int,input().split())
arr= []
for i in range(r):
	a = list(map(int,input().split()))
	arr.append((a))
for i in range(c):
	total = 0
	for j in range(r):
		total += arr[j][i]
	print(total, end=' ')
	
