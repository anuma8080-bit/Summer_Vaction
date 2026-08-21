p,m = map(int,input().split())
arr = []
people = []
for i in range(p):
	arr = input().split()
	if int(arr[1])>=m:
		people.append(arr[0])

print(len(people))
for i in range(len(people)):
	print(people[i],end=' ')