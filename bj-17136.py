import sys
sys.setrecursionlimit(10**6)

p = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]
count = float('inf')

def fill(x, y, size, value):
    for i in range(y, y + size):
        for j in range(x, x + size):
            p[i][j] = value

def check(x, y, size):
    if x + size > 10 or y + size > 10:
        return False
    for i in range(y, y + size):
        for j in range(x, x + size):
            if p[i][j] != 1:
                return False
    else: return True
    
def backtrack(pos, used):
    global count
    if pos == 100:
        count = min(count, used)
        return
    if used >= count:
        return
    x, y = divmod(pos, 10)
    if p[y][x] == 1:
        for i in range(5, 0, -1):
            if papers[i] > 0 and check(x, y, i):
                papers[i] -= 1
                fill(x, y, i, 0)
                backtrack(pos + 1, used + 1)
                fill(x, y, i, 1)
                papers[i] += 1
                
    else: backtrack(pos + 1, used)

backtrack(0, 0)
print(count if count != float('inf') else -1)