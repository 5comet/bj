import sys
t = int(input())
ans = []
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 and r1 == r2 : 
        ans.append('-1')
        continue
    
    distance = ((x1-x2)**2 + (y1-y2) **2)**0.5

    
    if -abs(r1 - r2) < distance < abs(r1 - r2): 
        ans.append('2')
        
    elif abs(r1 - r2) == distance or abs(r1 + r2) - distance == 0: ans.append('1')
    
    elif distance == 0 and r1 != r2 : ans.append('0')
print('\n'.join(ans))

