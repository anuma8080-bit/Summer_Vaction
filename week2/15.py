a = int(input())
nax = 0
start=0
end = 0
realstart = 0
realend = 0
realnax = 0
arr = list(map(int,input().split()))
for i in arr:
	if arr[i] == 1:
		start = i
		for j in range(i,a):
			if arr[j] == 0:
				end = j-1
				nax = end-start+1
				if nax>realnax:
					realend = end
					realnax = nax
					realstart = start
print(realnax, realstart, realend)