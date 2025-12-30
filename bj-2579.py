n = int(input())
l = [0]
l.extend(int(input()) for _ in range(n))
if n < 3 : print(l[-1] + l[-2]); exit()

dp = [0] * (n + 1)
dp[1] = l[1]
dp[2] = l[1] + l[2]
dp[3] = max(l[2] + l[3], l[1] + l[3])

for i in range(4, n + 1):
    dp[i] = max(dp[i-3] + l[i-1], dp[i-2]) + l[i]
    
print(dp[-1])