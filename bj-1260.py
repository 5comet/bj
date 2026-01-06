import sys
sys.setrecursionlimit(10000)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)] 
visDfs = [False] * (n + 1)
visBfs = [False] * (n + 1)
q = [v]
answer = [[], []]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
for k in range(1, n+1):
    graph[k].sort()

def dfs(v):
    visDfs[v] = True
    answer[0].append(str(v))
    for i in graph[v]:
        if not visDfs[i]:
            dfs(i)
            
def bfs(v):
    visBfs[v] = True
    answer[1].append(str(v))
    while q:
        v = q.pop(0)
        for i in graph[v]:
            if not visBfs[i]:
                q.append(i)
                visBfs[i] = True
                answer[1].append(str(i))

dfs(v)
bfs(v)
print(' '.join(answer[0]))
print(' '.join(answer[1]))