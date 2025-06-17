from collections import deque
import sys
input = sys.stdin.readline

def push_front(l, x):
    return l.appendleft(x)

def push_back(l, x):
    return l.append(x)

def pop_front(l):
    return print(-1) if len(l) == 0 else print(l.popleft())

def pop_back(l):
    return print(-1) if len(l) == 0 else print(l.pop())

def size(l):
    return print(len(l))

def empty(l):
    return print(1) if len(l) == 0 else print(0)

def front(l):
    return print(-1) if len(l) == 0 else print(l[0])

def back(l):
    return print(-1) if len(l) == 0 else print(l[-1])

dq = deque([])
n = int(input().rstrip())

for _ in range(n):
    a = input().split()
    if a[0] == 'push_front': push_front(dq, int(a[1]))
    elif a[0] == 'push_back': push_back(dq, int(a[1]))
    elif a[0] == 'pop_front': pop_front(dq)
    elif a[0] == 'pop_back': pop_back(dq)
    elif a[0] == 'size': size(dq)
    elif a[0] == 'empty': empty(dq)
    elif a[0] == 'front': front(dq)
    elif a[0] == 'back': back(dq)