longest_intersection = {'length': 0, 'numbers': None}

for _ in range(int(input())):
    first_set = set()
    second_set = set()
    first, second = input().split('-')
    first_start, first_end = first.split(',')
    second_start, second_end = second.split(',')

    for n in range(int(first_start), int(first_end) + 1):
        first_set.add(n)
    for n in range(int(second_start), int(second_end) + 1):
        second_set.add(n)
    intersection = first_set & second_set
    if len(intersection) > longest_intersection['length']:
        longest_intersection['length'] = len(intersection)
        longest_intersection['numbers'] = list(intersection)
print(f"Longest intersection is {longest_intersection['numbers']} with length {longest_intersection['length']}")