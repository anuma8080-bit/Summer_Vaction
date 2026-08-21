a = int(input())
arr = list(map(int,input().split()))
arr2 = []
for i in range(a):
	if arr[i] == 0:
		arr2.pop()
	else:
		arr2.append(arr[i])

print(sum(arr2))