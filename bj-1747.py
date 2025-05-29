import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_pal(n):
    s = str(n)
    if str(n) == s[::-1]:
        return True

n = int(input())

while True:
    if is_prime(n) and is_pal(n):
        print(n)
        break
    n += 1