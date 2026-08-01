a = int(input())
mon = 0
son = 0

b = list(map(int,input().split()))
for i in range(a):
	if b[i] > mon: 
			mon = b[i]
			son = i+1

print(mon, son)