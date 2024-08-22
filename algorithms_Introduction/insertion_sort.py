nums = [int(n) for n in input().split()]

i = 0

while i < len(nums) - 1:
    j = i + 1
    if nums[j] < nums[i]:
        nums[i], nums[j] = nums[j], nums[i]
        i -= 1
        if i < 0:
            i = 0
    else:
        i += 1
print(*nums)