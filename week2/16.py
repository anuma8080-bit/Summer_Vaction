a = int(input())
arr = [a]
for i in range(a):
	b,c = input().split()
	arr.append(b)
	arr.append(c)

f = int(input())
for i in range(f):
	d = input()
	if d in arr:
		for j in range(a*2):
			if arr[j] == d:
				print(arr[j+1])
	else:
		print(-1)
		