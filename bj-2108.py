import sys
from collections import deque
from collections import Counter
import statistics

def average():
    print(round(statistics.mean(numbers) + 10**-7))

def mid():
    print(statistics.median(numbers))

def mode():
    modes = Counter(numbers).most_common(2)
    if len(numbers) > 1 :
        if modes[0][1] == modes[1][1]:
            print(modes[1][0])
        else: print(modes[0][0])
    else: print(modes[0][0])

def ran():
    a = numbers[0]; b = numbers[-1]
    print(b - a)

n = int(input())
numbers = deque([int(sys.stdin.readline()) for _ in range(n)])
numbers = sorted(numbers)
sol = []

average()
mid()
mode()
ran()