s = input().strip()
current_s = s[0]
count = 1
for i in range(1, len(s)):
	if s[i] == current_s:
		count+=1
	else:
		print(f"{current_s}{count}", end=' ')	
		current_s = s[i]
		count = 1
print(f"{current_s}{count}",end=' ') 