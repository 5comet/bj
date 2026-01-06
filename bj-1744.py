import sys
input = sys.stdin.readline

n = int(input())
oneCount = 0; zeroCount = 0; maxSum = 0
plus = []
minus = []

for _ in range(n):
    k = int(input())
    if k == 1:
        oneCount += 1
    elif k > 1:
        plus.append(k)
    elif k < 0:
        minus.append(k)
    else: zeroCount += 1
        
plus.sort(reverse=True)
minus.sort()

if len(plus) > 1:
    for i in range(0, len(plus) - 1, 2):
        maxSum += plus[i] * plus[i + 1]
if len(plus) % 2 != 0:
    maxSum += plus[-1]

if len(minus) > 1:
    for i in range(0, len(minus) - 1, 2):
        maxSum += minus[i] * minus[i + 1]
if len(minus) % 2 != 0 and zeroCount == 0:
    maxSum += minus[-1]

print(maxSum + oneCount)