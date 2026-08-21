a = int(input())
arr  = []

for i in range(a):
	arr2 = input().split()
	cmd = arr2[0]
	if cmd == 'PUSH':
		arr.append(arr2[1])

	if cmd == 'POP':
		value = arr.pop()
		print(value)

	if cmd == 'SIZE':
		print(len(arr))



	
	