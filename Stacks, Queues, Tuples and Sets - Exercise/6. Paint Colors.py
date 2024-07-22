from collections import deque

colors = ("red", "yellow", "blue", "orange", "purple", "green")
secondary_colors = {"orange": ['red', 'yellow'], "purple": ['red', 'blue'], "green": ['yellow', 'blue']}
collected_colors = []

substrings_sequence = deque(input().split())

while substrings_sequence:
    first_substring = substrings_sequence.popleft()
    if substrings_sequence:
        second_substring = substrings_sequence.pop()
    else:
        second_substring = ''

    for color in colors:
        if first_substring + second_substring == color or second_substring + first_substring == color:
            collected_colors.append(color)
            break
    else:
        if first_substring[:-1] != '':
            substrings_sequence.insert(len(substrings_sequence) // 2, first_substring[:-1])
        if second_substring[:-1] != '':
            substrings_sequence.insert(len(substrings_sequence) // 2, second_substring[:-1])

for color in collected_colors:
    if color in secondary_colors:
        if not set(secondary_colors[color]).issubset(collected_colors):
            collected_colors.remove(color)

print(collected_colors)