a = int(input())
sa1 = 0
sa2 = 0
sa3 = 0
sa4 = 0
zero = 0
for i in range(a):
	b,c = map(int,input().split())
	if (b == 0 or c == 0):
		zero += 1
		continue
	if b>0:
		if c>0:
			sa1+=1
		else:
			sa2 += 1
	elif b<0:
		if c>0:
			sa4 += 1
		else:
			sa3 += 1


print(sa1,sa2,sa3,sa4,zero)
		