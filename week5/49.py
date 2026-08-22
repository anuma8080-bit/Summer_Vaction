a = int(input())
suc = True
res = []
arr = []
for i in range(a):
	n = list(map(int,input().split()))
	res.append(n)
	
res.sort()

for j in range(len(res) - 1):

    if res[j][1] > res[j + 1][0]:
        suc = False
        break

if suc:
	print("NO")
else:
	print("YES")