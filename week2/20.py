a = int(input())

arr = list(map(int,input().split()))
arr.sort()
arr2 = []
for i in arr:
	if i not in arr2:
		arr2.append(i)

for i in arr2:
	print(i, end=' ')
