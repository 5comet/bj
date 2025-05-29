from collections import deque
import sys
i = sys.stdin.readline

case = int(i().rstrip())
result = []

for _ in range(case):
    pt = 0
    n, m = map(int, i().split())
    a = deque(map(int, i().split()))
    y = m
    
    while a:
        imp = max(a)
        
        if a[0] == imp:
            a.popleft()
            pt += 1
            if y == 0: result.append(pt); break
            else : y -= 1
            
        else : 
            a.append(a.popleft())
            if y == 0 : y = len(a) - 1
            else : y -= 1
        
    
    deque.clear(a)

for k in result:
    print(k)