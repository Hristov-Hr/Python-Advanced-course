from collections import deque


def best_list_pureness(nums, num_k):

    numbers = deque(nums)
    max_total = 0
    count_rotation = 0
    for j in range(num_k + 1):
        total = 0
        for i in range(len(numbers)):
            total += numbers[i] * i
        if max_total < total:
            max_total = total
            count_rotation = j
        numbers.rotate(1)

    return f"Best pureness {max_total} after {count_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
