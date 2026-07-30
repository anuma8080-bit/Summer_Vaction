 #범위보다 낮은 갯수, 높은갯수 출력하는 문제
a,b,c = map(int,input().split())
arr = list(map(int, input().split()))
low = 0
high = 0
for i in arr:
	if i<b:
		low+=1
	elif i>c:
		high += 1

print(low, high)

