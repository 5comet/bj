import sys
from collections import deque

n = int(input())
x = deque([])
ranks = []

for _ in range(n):
    x.append(list(map(int, sys.stdin.readline().split())))

for _ in range(n):
    rank = 1
    for j in range(n-1):
        if x[0][0] < x[j+1][0] and x[0][1] < x[j+1][1]:
            rank += 1
    ranks.append(str(rank))
    x.rotate(-1)

print(' '.join(ranks))