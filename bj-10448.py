from itertools import combinations_with_replacement

nums = [int(i * (i + 1)/ 2) for i in range(1,45)]

com = []
for i in list(combinations_with_replacement(nums, 3)):
    if sum(i) < 1001:
        com.append(sum(i))
    else: pass
com = list(set(com))

ans = []
t = int(input())
for _ in range(t):
    a = int(input())
    if a in com: ans.append('1')
    else: ans.append('0')
    
print('\n'.join(ans))

