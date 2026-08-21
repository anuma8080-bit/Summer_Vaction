h,w = map(int,input().split())
sh,sw = map(int,input().split())
s = input()
arr = list(s)

for i in arr:
	if i == 'U':
		if sh > 1:
			sh-= 1
			
	if i == 'D':
		if sh < h:
			sh+= 1
			
	if i == 'R':
		if sw < w:
			sw+= 1
			
	if i == 'L':
		if sw > 1:
			shw-= 1
print(sh, sw)