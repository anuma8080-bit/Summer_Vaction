a,b =  map(int, input().split())
arr = list(map(int,input().split()))
total_arr = []
sun = 0
total_arr.append(0)
for i in range(len(arr)):
	sun+=arr[i]
	total_arr.append(sun)

for i in range(b):
	n,m = map(int,input().split())
	print(total_arr[m] - total_arr[n - 1])
