n = int(input())
s = ''
for i in range(1, n+1):
    s += str(i)
print(s.index(str(n))+1)