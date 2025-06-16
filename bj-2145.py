def p(n):
    i = sum(int(n[j]) for j in range(len(n)))
    if len(str(i)) == 1: return str(i)
    else: return p(str(i))
a = []
while 1:
    n = input()
    if n == '0' : break
    a.append(p(n))
print('\n'.join(a))