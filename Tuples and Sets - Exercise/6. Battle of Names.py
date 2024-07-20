odd_numbers = set()
even_numbers = set()

for i in range(1, int(input()) + 1):
    name_value = (sum([ord(char) for char in input()])) // i
    if name_value % 2 == 0:
        even_numbers.add(name_value)
    else:
        odd_numbers.add(name_value)

if sum(odd_numbers) > sum(even_numbers):
    print(*odd_numbers, sep=', ')
elif sum(odd_numbers) < sum(even_numbers):
    print(*even_numbers ^ odd_numbers, sep=', ')
elif sum(odd_numbers) == sum(even_numbers):
    print(*odd_numbers | even_numbers, sep=', ')