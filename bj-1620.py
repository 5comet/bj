import sys
from collections import defaultdict

n, m = map(int, input().split())
pokemon = defaultdict(list)
reversed_pokemon = defaultdict(list)
ans = []
    
for i in range(1, n + 1):
    name = sys.stdin.readline().rstrip()
    pokemon[name].append(i)
    reversed_pokemon[i] = name
    
for _ in range(m):
    x = sys.stdin.readline().rstrip()
    if x.isalpha(): ans.append(str(pokemon[x][-1]))
    else: ans.append(reversed_pokemon[int(x)])
    
print('\n'.join(ans))
