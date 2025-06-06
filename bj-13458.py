n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = len(a)
for i in range(n):
        d = a[i] - b
        if d < 1: continue
        d %= c
        cnt += (a[i] - b) // c
        while True:
                if d < 1: break 
                d -= c
                cnt += 1
print(cnt)