import sys
import math
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    clothes = {}
    
    for _ in range(m): 
        _, categoty = input().split()
        clothes[categoty] = clothes.get(categoty, 0) + 1
    
    count = [cnt + 1 for cnt in clothes.values()]
    result = math.prod(count) - 1
    
    print(result)
        