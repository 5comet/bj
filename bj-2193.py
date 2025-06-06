def pn(n):
    l = [1, 1]
    l.extend(l[i] + l[i+1] for i in range(n))
    return l[n-1]
print(pn(int(input())))
