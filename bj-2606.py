computer = int(input())
conn_computer = int(input())
conn_list = [[i] for i in range(1, computer+1)]

for _ in range(conn_computer):
    a, b = map(int, input().split())
    conn_list[a-1] += [b]
    conn_list[b-1] += [a]

virus = [1]
n = 0
visited = []
while True:
    if not virus: break
    v = virus.pop(0)
    
    if len(conn_list[v-1]) > 1 and v not in visited:
        virus.extend(conn_list[v-1][1:])
        
    if v not in visited:
        visited.append(v)
        n += 1
    
print(n-1)