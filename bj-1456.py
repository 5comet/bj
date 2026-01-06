a, b = map(int, input().split())
nums = [True for _ in range(int(b ** 0.5) + 1)]
cnt = 0

for i in range(2, len(nums)):
    if nums[i] == False: continue
    for j in range(i + i, int(b ** 0.5) + 1, i):
        nums[j] = False

for k in range(2, len(nums)):
    if nums[k] == False: continue
    z = 2
    while True:
        temp = k ** z
        if temp > b: break
        if a <= temp <= b: cnt += 1
        z += 1
print(cnt)