a,cp = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort(reverse = True)
for i in range(cp):
	arr[i]/=2

print(int(sum(arr)))