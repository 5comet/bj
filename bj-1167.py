import sys
from collections import deque
input = sys.stdin.readline

v = int(input())

nodes = [[] for _ in range(v + 1)]

for _ in range(1, v + 1):
    data = list(map(int, input().split()))
    u = data[0]
    for i in range(1, len(data) - 1, 2):
        end, weight = data[i], data[i + 1]
        nodes[u].append((end, weight))

def bfs(start):
    visited = [-1] * (v + 1) # 0 이상은 방문 / 거리로
    q = deque()
    
    visited[start] = 0
    q.append(start)
    MAX = 0
    f_node = start
    
    while q:
        next = q.popleft()
        
        for i in nodes[next]:
            if visited[i[0]] == -1:
                visited[i[0]] = visited[next] + i[1]
                q.append(i[0])
                
                if visited[i[0]] > MAX:
                    MAX = visited[i[0]]
                    f_node = i[0]
    return f_node, MAX

print(bfs(bfs(1)[0])[1])
