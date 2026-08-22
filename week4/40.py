a = int(input())
arr = list(map(int,input().split()))

for i in range(a):
	if i == 0:
		print(arr[0]+arr[1],end = ' ')
	elif i == a-1:
		print(arr[i-1]+arr[i],end = ' ')
	else:
		print(arr[i-1]+arr[i]+arr[1+i],end = ' ')

		