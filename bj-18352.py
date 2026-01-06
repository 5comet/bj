import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
cities = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    cities[a].append(b)
    
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] += 1
    while q:
        nxt = q.popleft()
        for i in cities[nxt]:
            if visited[i] == -1:
                visited[i] = visited[nxt] + 1
                q.append(i)
            
bfs(x)

for i in range(n + 1):
    if visited[i] == k:
        answer.append(str(i))
        
print(-1 if not answer else '\n'.join(answer))
