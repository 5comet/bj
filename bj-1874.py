import sys

input = sys.stdin.readline

n = int(input().rstrip())
target = [int(input().rstrip()) for _ in range(n)]

stack = []
sequence = []
answer = []
number = 1
index = 0

while True:
    if len(sequence) == n or number > n+1 : break
    
    if len(stack) > 0 and stack[-1] == target[index]:
        sequence.append(stack.pop())
        answer.append('-')
        index += 1
        
    else : 
        stack.append(number)
        answer.append('+')
        number += 1

print('\n'.join(answer)) if list(sequence) == target else print('NO')
    
    

