a = int(input())
scores  = {}
for i  in range(a):
	name,score =  input().split()
	scores[name] =  int(score)

scores = sorted(scores.items(), key=lambda x: (-x[1],x[0]))


for name, score in scores:
	print(name)