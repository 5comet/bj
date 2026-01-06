import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
time = [list(map(int, input().split())) for _ in range(n)]
time.sort(key= lambda x : (x[1], x[0]))
end = -1

for i in range(n):
    if time[i][0] >= end:
        end = time[i][1]
        cnt += 1
print(cnt)