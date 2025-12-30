n = int(input())
m = int(input())

nums = sorted(map(int, input().split()))

left = 0
right = n - 1
count = 0

while left < right:
    if nums[left] + nums[right] < m:
        left += 1
    elif nums[left] + nums[right] > m:
        right -= 1
    else:
        count += 1
        left += 1
        right -= 1

print(count)