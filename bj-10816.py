import sys
from collections import Counter

n = int(input())
card = Counter(map(int, sys.stdin.readline().split()))
m = int(input())
cp = list(map(int, sys.stdin.readline().split()))
s = []
s.extend(str(card[j]) for j in cp)
print(' '.join(s))
