import math

def is_prime(x):
    if x == 1 : return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True 
n,m = map(int, input().split())
sol = []
for _ in range(m - n + 1):
    if is_prime(n) == True: sol.append(str(n))
    n += 1
print('\n'.join(sol))
