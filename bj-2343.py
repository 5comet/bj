import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
lecs = list(map(int, input().split()))
s_idx = max(lecs)
e_idx = sum(lecs)

while s_idx <= e_idx:
    mid = int((s_idx + e_idx) / 2)
    s = 0
    cnt = 0
    for i in lecs:
        if s + i > mid:
            cnt += 1
            s = 0
        s += i
    if s != 0 : cnt += 1
    
    if cnt > m:
        s_idx = mid + 1
    else:
        e_idx = mid - 1
    
print(str(s_idx))