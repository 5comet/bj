import sys
input = sys.stdin.readline

t = int(input().rstrip())
ans = []

for _ in range(t):
    a = map(int,input().split())
    ans.append(str(min(a)))
print('\n'.join(ans))