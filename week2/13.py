a = int(input())
arr = []
for i in range(a):
	b = input()
	if b not in arr:
		arr.append(b)
print(len(arr))
for i in range(len(arr)):
	print(arr[i], end=' ')