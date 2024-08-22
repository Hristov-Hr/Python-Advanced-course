universe = set(input().split(', '))
sets_as_list = []

for _ in range(int(input())):
    sets_as_list.append(input().split(', '))

result = []

while universe:
    current_subset = []
    for s in sets_as_list:
        subset = set(s)
        current_subset.append([s, len(universe.intersection(subset))])
    biggest_subset = sorted(current_subset, key=lambda x: -x[1])[0][0]
    result.append(biggest_subset)
    universe.difference_update(biggest_subset)

print(f"Sets to take ({len(result)}):")
[print('{ ' + f"{', '.join(x)}" + ' }') for x in result]
