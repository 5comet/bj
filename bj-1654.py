import sys

k, n = map(int, input().split())

lan = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(lan)
max = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(cable // mid for cable in lan)
    
    if total >= n:
        max = mid  
        start = mid + 1  
    else:
        end = mid - 1

print(max)