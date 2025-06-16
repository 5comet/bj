from collections import Counter
n = int(input())
ans = []
for _ in range(n):
    a, b = map(Counter, input().split())
    if a == b: ans.append('Possible')
    else: ans.append('Impossible')
print('\n'.join(ans))