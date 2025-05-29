# 괄호검사
def cm(a):
    stack = []
    for i in a:
        stack.append(i)
        if i == ')' :
            if '(' in stack: 
                stack.remove('(')
                stack.remove(')')
    if stack == [] : return 'YES'
    else: return 'NO'

st = []
for _ in range(int(input())):
    st.append(cm(list(input())))
for result in st:
    print(result)