r,c, n= map(int, input().split())
rr = 1
rc = n-c
while n-c> c:
	rr=+1
	rc = n-c
	n=-c
if(rr>r or rc>c):
	print(-1)
else:
	print(rr+1, rc)
