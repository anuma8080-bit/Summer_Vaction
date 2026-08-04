a = int(input())
result = [0]*1001
arr = list(map(int,input().split()))
for i in range(a):
	
	result[arr[i]]+=1

for i in range(1000):
	if result[i] != 0:
		print(i, result[i])