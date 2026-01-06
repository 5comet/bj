mn, mx = map(int, input().split())
check = [False] * (mx - mn + 1)

for i in range(2, int(mx ** 0.5) + 1):
    p = i * i
    start = int(mn / p) if mn % p == 0 else int(mn / p) + 1
    
    for j in range(start, int(mx / p) + 1):
        check[p * j - mn] = True
        
print(check.count(False))