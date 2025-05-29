import sys
from collections import deque
def is_balanced(list):
    a = deque([])
    for c in list:
        if c in ['(', '[']:
            a.appendleft(c)
        elif c == ')':
            if len(a) != 0 and a[0] == '(':
                a.remove('(')
            else : a.appendleft(c)
        elif c == ']':
            if len(a) != 0 and a[0] == '[':
                a.remove('[')
            else : a.appendleft(c)
    if len(a) == 0: return 'yes'
    else: return 'no'
    
s = []
while True:
    string = sys.stdin.readline().rstrip()
    if string == '.': break
    s.append(is_balanced(list(string)))

print('\n'.join(s))