a = int(input())

arr = list(map(int,input().split()))

n = int(input())
arr2 = list(map(int,input().split()))
for i in range(n):
	if arr2[i] not in arr:
		print('-1',end = ' ')
	else:
		for j in range(a):
			if arr[j] == arr2[i]:
				print(j+1,end= ' ')