n = int(input())
l = [int(input()) for _ in range(n)]
l.sort()
a = l[0]
for i in range(n-1):
    a += l[i+1]
    a /= 2
print(a)