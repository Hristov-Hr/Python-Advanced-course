from typing import List


def list_manipulator(nums: List, first: str, second: str, *args):

    if first == 'add':
        if second == 'end':
            [nums.append(a) for a in args]
        else:
            [nums.insert(0, a) for a in args[::-1]]

    else:
        idx = args[0] if args else 1
        if second == 'end':
            nums = nums[:len(nums) - idx]
        else:
            nums = nums[idx:]

    return nums


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
