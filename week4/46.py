a,b = map(int,input().split())
temp = 0
next = 0
current = 0
arr = list(map(int,input().split()))
for i in range(b):
	current = arr[0]
	next = arr[0]
	for j in range(1,a):
		
		current = arr[j]
		arr[j] = next
		next = current
		if j == a-1:
			arr[0] = current


for i in range(len(arr)):
	print(arr[i], end=' ')