import sys

n, m = map(int, input().split())
num = list(map(int, input().split()))
numbersum= [0]

for k in range(len(num)):
    numbersum.append(numbersum[k]+num[k])
ans = []

for _ in range(m):
    i, j = map(int, input().split())
    i -= 1 
    ans.append(str(numbersum[j] - numbersum[i]))

print('\n'.join(ans))