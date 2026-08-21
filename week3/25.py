r,c = map(int,input().split())
arr = []
for i in range(r):
	a = list(map(int,input().split()))
	arr.append(a)
for i in range(c):
	for j in range(r):
		print(arr[j][i], end = ' ')
	print()