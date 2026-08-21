a,b =  map(int, input().split())
arr = list(map(int,input().split()))
sun = 0
for i in range(b):
	sun = 0
	s,e = map(int, input().split())
	for i in range(s,e+1):
		sun+=arr[i-1]
	print(sun)