import sys
from collections import deque
s = input()

left = deque(s)
right = deque(list())

m = int(sys.stdin.readline().rstrip())

for _ in range(m):
    inp = sys.stdin.readline().split()

    if inp[0] == 'L':
        if len(left) == 0: pass
        else: right.appendleft(left.pop())
    
    elif inp[0] == 'D':
        if len(right) == 0: pass
        else: left.append(right.popleft())
    
    elif inp[0] == 'B':
        if len(left) == 0: pass
        else: left.pop()
    
    elif inp[0] == 'P':
        left.append(inp[1])

left.extend(right)
print(''.join(list(left)))