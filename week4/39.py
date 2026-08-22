a,b = map(int,input().split())
arr = []
sun = 0
for i in range(a):
	c = list(map(int,input().split()))
	arr.append(c)

for i in range(a):
	for j in range(b):
		if i == 0 or j == 0 or i+1 == a or j+1 ==b:
			sun += arr[i][j]
print(sun)