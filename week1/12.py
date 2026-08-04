a = int(input())
arr = list(map(int,input().split()))
count = 0
for i in range(a):
	if (sum(arr) / len(arr))<arr[i]:
		count +=1

print(count)