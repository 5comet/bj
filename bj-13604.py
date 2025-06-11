j, r = map(int, input().split())
score = list(map(int, input().split()))
scores = [0 for _ in range(j)]

for i in range(len(score)):
    scores[i % j] += score[i]

if scores.count(max(scores)) > 1:
    print(max(list(filter(lambda x : scores[x] == max(scores), range(j))))+1)

else: print(scores.index(max(scores)) + 1)    