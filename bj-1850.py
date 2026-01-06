def gcd(a, b):
    mx = max(a, b)
    mn = min(a, b)
    while True:
        temp = mx % mn
        if temp == 0: return mn
        mx = mn
        mn = temp
a, b = map(int, input().split())
print('1' * gcd(a, b))