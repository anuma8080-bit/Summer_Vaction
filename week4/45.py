arr = list(input())

n = int(input())

for i in range(n):
	alp = input()
	if alp not in arr:
		print('-1',end = ' ')
	else:
		for j in range(len(arr)):
			if alp == arr[j]:
				print(j+1)
				break