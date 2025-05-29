t = int(input())
ans = []
for _ in range(t):
    box = 0
    cnt = 0
    move = 0
    grid = []
    m, n = map(int, input().split())
    for _ in range(m):
        grid.append(list(map(int,input().split())))
    rotated_grid = list(map(list, zip(*grid)))
    
    for i in rotated_grid:
        for j in i:
            if j == 1: 
                cnt += m - i.index(j) - i.count(1)
                i[i.index(j)] = 2
    ans.append(str(cnt))
                

print('\n'.join(ans))
