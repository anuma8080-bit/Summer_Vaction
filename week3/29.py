a = int(input())
count = {}

for i in range(a):
	name,sik = input().split('.')
	if sik in count:
		count[sik] += 1
	else:
		count[sik] = 1

counts = sorted(count.items(), key=lambda x: x[0])

for name, sik in counts:
	print(name, sik)