a = int(input())
arr = []

for i in range(a):
	arr2 = list(input().split())
	if arr2[0] == "UNDO":
		arr.pop()
	else:
		arr.append(arr2[1])

for i in range(len(arr)):
	print(arr[i],end='')