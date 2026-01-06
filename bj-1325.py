import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True
    cnt = 1
    
    while q:
        nxt = q.popleft()
        for i in cc[nxt]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt

n, m = map(int, input().split())
cc = [[] for _ in range(n + 1)]
answer = []
maxvl = -1

for _ in range(m):
    a, b = map(int, input().split())
    cc[b].append(a)

for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt > maxvl:
        maxvl = cnt
        answer = [i]
    elif cnt == maxvl:
        answer.append(i)

print(*(answer))
