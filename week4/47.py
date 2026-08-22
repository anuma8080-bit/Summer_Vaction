a = int(input())
arr = list(range(1, a + 1))
while len(arr)>1:
	arr.pop(0)
	arr.append(arr.pop(0))
print(arr[0])