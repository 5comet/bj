def clock(x):
    nums = [x]
    while True:
        x += x[0]
        x = x[1:]
        if x in nums : break
        nums.append(x)
    return int(min(nums))

n = input().replace(' ', '')
n = int(clock(n))
ans = [n]

while True:
    if n == 1111 : break
    n -= 1
    if '0' not in str(n) and clock(str(n)) == n:
        ans.append(n)
print(len(ans))