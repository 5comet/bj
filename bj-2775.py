def apt(list):
    l = [0 for _ in range(n)]
    for i in range(n):
        l[i] = sum(list[:i+1])
    return l
        
t = int(input())
sol = []

for _ in range(t):
    k = int(input())
    n = int(input())
    fz = list(range(1,n+1))
    for _ in range(k):
        fz = apt(fz)
    sol.append(str(fz[n-1]))

print('\n'.join(sol))