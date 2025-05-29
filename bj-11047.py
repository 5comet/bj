import sys
n, k = map(int, input().split())
cnt = 0

coin = [int(input()) for _ in range(n)]
if n == 1 and coin[0] == 1 : print(k); exit()
coin.sort(reverse=True)

while k != 0:
    for i in coin:
        if k >= i:
            cnt += k // i
            k %= i
print(cnt)