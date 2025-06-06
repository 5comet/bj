def fibo(x):
    fib = [0, 1]
    fib.extend((fib[i] + fib[i + 1]) % 1000000000 for i in range(abs(x)-1))
    if x < 0:
        if abs(x) % 2 == 0: return -fib[abs(x)]
        else: return fib[abs(x)]
    else: return fib[abs(x)]
    
n = fibo(int(input()))
if n > 0 : print(1)
elif n == 0 : print(0)
elif n < 0 : print(-1)

print(abs(n))