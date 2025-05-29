def count_fib(max_n):
    zero = [1, 0]
    one = [0, 1]
    
    for i in range(2, max_n+1):
        zero.append(zero[i-1] + zero[i-2])
        one.append(one[i-1] + one[i-2])
    
    return zero, one

t = int(input())
cases = [int(input()) for _ in range(t)]
max_n = max(cases) 

zero, one = count_fib(max_n)

results = [f"{zero[n]} {one[n]}" for n in cases]
print('\n'.join(results))
