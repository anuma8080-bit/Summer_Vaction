open =0
close = 0
stack = []
str = input()
arr = list(str)
ok = True
for i in arr:
	if i == '(':
		stack.append(i)
	else:
		if not stack:
			ok = False
			break
		
		stack.pop()

if ok:
	print("YES")
else:
	print("NO")