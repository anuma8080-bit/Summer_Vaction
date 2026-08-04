arr = input()
inn = input()
count=0
for i in range(len(arr)):
	if arr[i] == inn:
		count+=1

print(count)