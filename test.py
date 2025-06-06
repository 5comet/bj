al = ['A', 'B', 'C', 'D', 'E', 'F']
chess = [[0 for _ in range(6)] for _ in range(6)]
a = 0
for _ in range(36):
        m = input()
        if chess[int(m[1])-1][al.index(m[0])] == 0: 
                chess[int(m[1])-1][al.index(m[0])] = 1
        else: a = 1
if a != 0 and 0 in chess: print('Invalid')
else: print('Valid')

