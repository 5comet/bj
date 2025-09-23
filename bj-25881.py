r, e = map(int,input().split())
n = int(input())
u = []
bill = []
for _ in range(n):
    i = int(input())
    u.append(i)
    if i > 1000:
        j = i - 1000
        bill.append((i - j) * r + (j * e))
    else: bill.append(i * r)

for i in range(n):
    print(u[i], bill[i])