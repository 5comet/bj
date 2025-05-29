n = int(input())
room = [list(input()) for _ in range(n)]
room2 = list(map(list, zip(*room[::-1])))
row = 0; col = 0

for i in room:
    cnt = 0
    for j in i:
        if j == '.':
            cnt += 1
        elif j == 'X': cnt = 0
        
        if cnt == 2:
            row += 1
            

for i in room2:
    cnt = 0
    for j in i:
        if j == '.':
            cnt += 1
        elif j == 'X': cnt = 0
        
        if cnt == 2:
            col += 1

print(row, col)