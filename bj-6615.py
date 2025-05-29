def collatz(n):
    l = [n]
    while True:
        if n == 1 : break
        if n % 2 == 0 : n //=2
        else: n = n * 3 + 1
        l.append(n)
    return l

ans = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0: break
    al = collatz(a); bl = collatz(b)
    c = list(set(al) & set(bl))[0]
    aindex = al.index(c) ; bindex = bl.index(c)
    
    ans.append(f'{a} needs {aindex} steps, {b} needs {bindex} steps, they meet at {c}')
    
print('\n'.join(ans))
    
    #https://www.acmicpc.net/problem/6615