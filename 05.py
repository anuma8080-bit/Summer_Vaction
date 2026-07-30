n,s = map(int,input().split())
arr = list(map(int,input().split()))
count = 0
for i in range(len(arr)):
	if arr[i] == 0:
		count += 1
	elif arr[i] %s ==0:
		count += 1
	elif arr[i] == 0:
		count += 1
print(count)