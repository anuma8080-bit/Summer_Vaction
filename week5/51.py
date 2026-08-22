mon = int(input())
five = 0
hun = 0
fiveten = 0
ten = 0
sun=0
while mon != 0:
	if mon >=500:
		mon-=500
		five+=1
		sun+=1
	elif mon >= 100:
		mon -= 100
		hun += 1
		sun+=1
	elif mon >= 50:
		mon -= 50
		fiveten += 1
		sun+=1
	elif mon>= 10:
		mon -= 10
		ten+=1
		sun+=1

print(sun)
print(five, hun, fiveten, ten)