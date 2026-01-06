import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))

d = deque()
idx = deque()
answer = []

for i in range(n):
    d.appendleft(a[i])
    idx.appendleft(i)
    check = d[0]
    
    while not len(d) <= 1:
        if check >= d[1]:
            break
        d.remove(d[1])
        idx.remove(idx[1])
        
    if idx[-1] <= i - l :
        d.pop()
        idx.pop()
    answer.append(d[-1])


print(' '.join(map(str, answer)))