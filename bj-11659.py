import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sumlist = [0] * (n + 1)
ans = []

for i in range(1, n + 1):
    sumlist[i] = sumlist[i-1] + nums[i-1]

for _ in range(m):
    s, e = map(int, input().split())
    ans.append(str(sumlist[e] - sumlist[s - 1]))
    
print('\n'.join(ans))