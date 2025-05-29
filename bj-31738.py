def fac(n, m):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % m
    return result 

n, m = map(int, input().split())
print(0) if n > m else print(fac(n, m))