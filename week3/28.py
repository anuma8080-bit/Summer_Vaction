a = int(input())
arr = list(map(int,input().split()))
max_len = 1
length=0
for i in range(1, len(arr)):
	if arr[i]>arr[i-1]:
		length+=1
	else :
		if length>max_len:
			max_len = length
		length = 1

if length>max_len:
			max_len = length
print(max_len)