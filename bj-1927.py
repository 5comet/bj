import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
numbers = []
ans = []

for _ in range(n):
    m = int(input().rstrip())
    
    if m == 0:
        if len(numbers) == 0:
            ans.append('0')
        else: ans.append(str(heapq.heappop(numbers)))
        
    else: 
        heapq.heappush(numbers, m)
            
    
print('\n'.join(ans))
