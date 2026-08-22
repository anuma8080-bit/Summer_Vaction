a = int(input())
arr = list(map(int,input().split()))
arr.sort()
total_arr = []
sun =0
total_sum = 0
for i in range(a):
	sun+=arr[i]
	total_arr.append(sun)

for i in range(a):
	total_sum += total_arr[i]

print(total_sum)