c,max = map(int, input().split())
arr = list(map(int, input().split()))
total = 0
discount = 0
for i in arr:
	total += i

if total>max:
	discount = total-max
	print(max, discount)

else :
	print(total, discount)