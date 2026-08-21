a= int(input())
arr1 = list(input().split())
b= int(input())
arr2 = list(input().split())
arr3 = []
for i in arr2:
	 if i in arr1:
		 arr3.append(i)

print(len(arr3))
for i in arr3:
	print(i,end=' ')