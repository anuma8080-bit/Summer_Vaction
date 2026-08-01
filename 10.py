a = int(input())
st = ""
lon = 0
for i in range(a):
	b = input()
	if len(b) > lon: 
		lon = len(b)
		st = b

print(st, lon)