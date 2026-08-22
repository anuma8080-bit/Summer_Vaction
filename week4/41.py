a = int(input())
arr = list(map(int,input().split()))
nax = 0
for i in range(a):
	if arr[i] > nax:
		nax = arr[i]
	print(nax,end = ' ')