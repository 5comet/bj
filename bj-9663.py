import sys
sys.setrecursionlimit(10**6)

n = int(input())

cnt = 0

col = [False] * n
d1 = [False] * (2 * n - 1)
d2 = [False] * (2 * n - 1)

def bt(r):
    global cnt
    if r == n:
        cnt += 1
        return
    
    for i in range(n):
        if not col[i] and not d1[r + i] and not d2[r - i + n - 1]:
            col[i] = d1[r + i] = d2[r - i + n - 1] = True
            bt(r + 1)
            col[i] = d1[r + i] = d2[r - i + n - 1] = False
            
bt(0)
print(cnt)
