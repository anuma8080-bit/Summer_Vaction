a = int(input())
arr = list(input().split())
cards = {}
for i in range(a):
	if arr[i] in cards:
		cards[arr[i]]+=1
	else:
		cards[arr[i]] = 1
b = int(input())
arr2 = list(input().split())
for i in arr2:
	print(cards.get(i, 0), end=' ')