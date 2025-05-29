n, k = map(int, input().split())
days = list(map(int, input().split()))
tem = sum(days[:k])
maxtem = tem
for i in range(n - k):
    tem = tem - days[i] + days[i + k]
    if maxtem < tem: maxtem = tem

print(maxtem)