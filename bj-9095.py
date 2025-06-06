def ott(x):
    dp = [1, 2, 4]
    dp.extend(dp[i] + dp[i - 1] + dp[i - 2] for i in range(2, x))
    return str(dp[x-1])
t = int(input())
ans = [ott(int(input())) for _ in range(t)]
print('\n'.join(ans))
