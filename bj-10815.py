n = int(input())
hc = input().split()

m = int(input())
ishave = input().split()
ishaved = {}

for a in ishave:
    ishaved[a] = '0'

s = set(hc) & set(ishave)
for i in s:
    ishaved[i] = '1'
    
print(*ishaved.values())