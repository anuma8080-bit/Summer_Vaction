a = int(input())
scores = {}
for i in range(a):
	team,score = input().split()
	score = int(score)
	if team in scores:
		scores[team] += score
	else:
		scores[team] = score

for i in sorted(scores.keys()):
	print(i,scores[i])