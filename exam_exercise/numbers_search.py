def numbers_searching(*args):

    min_number = min(args)
    max_number = max(args)
    missing_numbers = []
    duplicate_nums = set()

    for num in range(min_number, max_number + 1):
        if num not in args:
            missing_numbers.append(num)
            continue
        if args.count(num) > 1:
            duplicate_nums.add(num)

    missing_numbers.append(list(sorted(duplicate_nums)))

    return missing_numbers


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
