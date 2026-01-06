import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())

f = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
arrive = False

def dfs(v, d):
    global arrive
    if d == 5:
        arrive = True
        return
    
    visited[v] = True
    for i in f[v]:
        if not visited[i]:
            dfs(i,d + 1)
    visited[v] = False # 양방향이라서 false로 다시 바꿔줌
            
for _ in range(m):
    s, e = map(int, input().split())
    f[s].append(e)
    f[e].append(s)

for i in range(n):
    dfs(i,1)
    if arrive: break

if arrive: print(1)
else: print(0)


