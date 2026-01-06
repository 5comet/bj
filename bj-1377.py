import sys
input = sys.stdin.readline

n = int(input())
nums = [(int(input()), i) for i in range(n)]

sortedNums = sorted(nums)
m = 0
for j in range(n):
    m = max(m, sortedNums[j][1] - j)
    
print(m+1)
