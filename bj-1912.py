n = int(input())
l = list(map(int, input().split()))
dp = [l[0]]
dp.extend(max(dp[i-1] + l[i], l[i] + l[i-1], l[i]) for i in range(1, len(l)))
print(max(dp))