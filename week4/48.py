a = int(input())
arr = []

for i in range(a):
	n = int(input())
	if n==0:
		if not arr :
			print(-1)
		else:
			
			print(arr.pop(arr.index(max(arr))))
	else:
		arr.append(n)