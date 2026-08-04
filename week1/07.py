a = int(input())
arr = list(map(int, input().split()))
z=0
h=0

for i in range(a):
	if arr[i] % 2 == 0:
		z+=arr[i]
	else:
		h+=arr[i]

print(z,h)