c,r = map(int,input().split())
arr = []
for i in range(c):
	a = list(map(int,input().split()))
	arr.append(sum(a))


for i in arr:
	print(i,end=' ')