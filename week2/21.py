a = int(input())
festivals = []
for i in range(a):
	b,c,d = input().split()
	
	festivals.append((int(c),int(d),b))
festivals.sort()

for i in festivals:
	print(i[2],end = ' ')
	