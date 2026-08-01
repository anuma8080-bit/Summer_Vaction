moem = ["a","e","i","o","u"]
arr = input()
count=0
for i in range(len(arr)):
	if arr[i] in moem:
		count+=1

print(count)