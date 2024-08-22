nums = [int(n) for n in input().split()]

n = len(nums) - 1

while n >= 0:
    for i in range(n):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    n -= 1

print(*nums)