import sys
n = int(input())
if n == 0: print(0); exit()
p = round(n * 0.15+10**-7)
lev = []
for _ in range(n):
    lev.append(int(sys.stdin.readline().rstrip()))
if len(lev) > 2: lev = sorted(lev)[p:n-p]
print(round((sum(lev) / len(lev))+10**-7))