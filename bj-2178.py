import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        maze[i][j] = int(maze[i][j])
        
def bfs(x, y):
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        nxt = q.pop(0)
        for i in range(4):
            x = nxt[0] + dx[i]
            y = nxt[1] + dy[i]
            if x >= 0 and y >= 0 and x < n and y < m:
                if maze[x][y] != 0 and visited[x][y] != True:
                    visited[x][y] = True
                    maze[x][y] = maze[nxt[0]][nxt[1]] + 1
                    q.append((x, y))

bfs(0, 0)
print(maze[n - 1][m - 1])
    