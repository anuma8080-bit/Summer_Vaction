a = int(input())
arr = list(map(int,input().split()))

n = int(input())
arr2 = list(map(int,input().split()))

for i in range(n):
	if arr2[i] in arr:
		print("YES")
	else:
		print("NO")