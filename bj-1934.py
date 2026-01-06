def gcd(a, b):
    mx = max(a, b)
    mn = min(a, b)
    while True:
        temp = mx % mn
        if temp == 0: return int(a * b / mn)
        mx = mn
        mn = temp

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(gcd(a, b))