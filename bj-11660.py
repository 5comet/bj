import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [[0] * (n + 1)]
nums.extend([0] + list(map(int, input().split())) for _ in range(n))
sumlist = [[0] * (n + 1) for _ in range(n + 1)]


for i in range(1, n + 1):
    for j in range(1, n + 1):
        sumlist[i][j] = sumlist[i-1][j] + sumlist[i][j-1] - sumlist[i-1][j-1] + nums[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = sumlist[x2][y2] - sumlist[x1-1][y2] - sumlist[x2][y1-1] + sumlist[x1-1][y1-1]
    print(answer)