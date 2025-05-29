import sys

def add(x):
    if x in S: return 
    S.append(x)

def remove(x):
    if x not in S: return
    S.remove(x)

def check(x):
    if x in S: print(1)
    else: print(0)
    

def toggle(x):
    if x in S: S.remove(x)
    else: S.append(x)

S = []

m = int(input())
for _ in range(m):
    order = sys.stdin.readline().rstrip()
    
    if order.split()[0] == 'add' : add(int(order.split()[-1]))
    
    elif order.split()[0] == 'remove' : remove(int(order.split()[-1]))
    
    elif order.split()[0] == 'check' : check(int(order.split()[-1]))
    
    elif order.split()[0] == 'toggle' : toggle(int(order.split()[-1]))
    
    elif order.split()[0] == 'all' : S = list(range(1,21))
    
    elif order.split()[0] == 'empty' : S.clear()