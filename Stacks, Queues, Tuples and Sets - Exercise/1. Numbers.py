first_line_numbers = set(int(x) for x in input().split())
second_line_numbers = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, second_command, *numbers = input().split()
    operation = first_command + second_command

    if operation == 'AddFirst':
        [first_line_numbers.add(int(num)) for num in numbers]
    elif operation == 'AddSecond':
        [second_line_numbers.add(int(num)) for num in numbers]
    elif operation == 'RemoveFirst':
        [first_line_numbers.remove(int(num)) for num in numbers if int(num) in first_line_numbers]
    elif operation == 'RemoveSecond':
        [second_line_numbers.remove(int(num)) for num in numbers if int(num) in second_line_numbers]
    elif operation == 'CheckSubset':
        print(first_line_numbers.issubset(second_line_numbers) or second_line_numbers.issubset(first_line_numbers))

print(*sorted(first_line_numbers), sep=', ')
print(*sorted(second_line_numbers), sep=', ')


# solution 2:

# first_line_numbers = set(int(x) for x in input().split())
# second_line_numbers = set(int(x) for x in input().split())
#
# functions = {
# 'AddFirst': lambda x: [first_line_numbers.add(int(num)) for num in x],
# 'AddSecond': lambda x: [second_line_numbers.add(int(num)) for num in x],
# 'RemoveFirst': lambda x: [first_line_numbers.remove(int(num)) for num in x if int(num) in first_line_numbers],
# 'RemoveSecond': lambda x: [second_line_numbers.remove(int(num)) for num in x if int(num) in second_line_numbers],
# 'CheckSubset': lambda x: print(first_line_numbers.issubset(second_line_numbers) or second_line_numbers.issubset(first_line_numbers))
# }
#
# for _ in range(int(input())):
#     first_command, second_command, *numbers = input().split()
#     operation = first_command + second_command
#     functions[operation](numbers)
#
#
# print(*sorted(first_line_numbers), sep=', ')
# print(*sorted(second_line_numbers), sep=', ')