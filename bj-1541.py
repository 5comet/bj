def mySum(string):
    SUM = 0
    string = string.split('+')
    for i in string:
        if i.isnumeric():
            SUM += int(i)
    return SUM
    
ans = 0
a = input().split('-')

for i in range(len(a)):
    if i == 0:
        ans += mySum(a[i])
    else : ans -= mySum(a[i])
print(ans)