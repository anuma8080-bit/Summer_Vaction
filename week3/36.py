a = int(input())
arr = list(map(int,input().split()))
sun = 0
for i in range(a):
	sun += arr[i]
	print(sun,end=' ')