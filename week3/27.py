a, s = map(int,input().split())
arr = ['O' for i in range(a)]
arr2 = list(map(int,input().split()))
for i in arr2:
	arr[i-1] = 'X'

for i in arr:
	print(i,end='')