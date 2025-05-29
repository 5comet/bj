import sys
input = sys.stdin.readline

n = int(input().rstrip())
hills = list(map(int, input().split()))

killstreak = []
maxhill = 0
count = 0

for hill in hills:
    if hill > maxhill :
        maxhill = hill
        killstreak.append(count)
        count = 0
    else : count += 1
killstreak.append(count)

print(max(killstreak))