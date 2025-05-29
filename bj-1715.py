import sys
from heapq import *

def com(cards):
    result = 0
    heapify(cards)
    while len(cards) > 1:
        c = heappop(cards) + heappop(cards)
        result += c
        heappush(cards, c)
        
    return result
        
input = sys.stdin.readline
n = int(input().rstrip())
cards = [int(input().rstrip()) for _ in range(n)]

print(com(cards)) if n != 1 else print(0)