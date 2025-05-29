def pr(op):
    if op in ['(' , ')']: return 0
    elif op in ['+', '-']: return 1
    elif op in ['*', '/']: return 2
    else: return -1
    
def change(l):
    result = []
    stack = []
    
    for i in l:
        if i.isalpha():
            result.append(i)
        else:
            if i == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            elif i == '(':
                stack.append(i)
            else:
                while stack and stack[-1] != '(' and pr(i) <= pr(stack[-1]):
                    result.append(stack.pop())
                stack.append(i)
    
    while stack:
        result.append(stack.pop())
    
    return result

a = list(input())
ca = change(a)
print(''.join(ca))
        