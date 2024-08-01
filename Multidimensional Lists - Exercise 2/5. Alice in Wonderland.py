size = int(input())
wonderland_territory = []
alice_position = []
collected_bags = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(size):
    wonderland_territory.append([int(x) if x.isdigit() else x for x in input().split()])
    if 'A' in wonderland_territory[r]:
        alice_position = [r, wonderland_territory[r].index('A')]
        wonderland_territory[alice_position[0]][alice_position[1]] = "*"

while collected_bags < 10:
    row, col = directions[input()]
    alice_position[0] += row
    alice_position[1] += col
    if not 0 <= alice_position[0] < size or not 0 <= alice_position[1] < size:
        break
    if wonderland_territory[alice_position[0]][alice_position[1]] == 'R':
        wonderland_territory[alice_position[0]][alice_position[1]] = '*'
        break
    elif wonderland_territory[alice_position[0]][alice_position[1]] != '.' \
            and wonderland_territory[alice_position[0]][alice_position[1]] != '*':
        collected_bags += int(wonderland_territory[alice_position[0]][alice_position[1]])
    wonderland_territory[alice_position[0]][alice_position[1]] = '*'

print("Alice didn't make it to the tea party.") if collected_bags < 10 else print('She did it! She went to the party.')
[print(*r) for r in wonderland_territory]