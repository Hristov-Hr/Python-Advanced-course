nums = [int(n) for n in input().split()]

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[i]:
            nums[i], nums[j] = nums[j], nums[i]

print(*nums)