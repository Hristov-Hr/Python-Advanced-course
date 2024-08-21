def recursive_sum_calculate(nums):
    if len(nums) == 0:
        return 0
    return nums.pop() + recursive_sum_calculate(nums)


print(recursive_sum_calculate([int(i) for i in input().split()]))