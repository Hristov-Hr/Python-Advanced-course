from collections import deque


def check_index(position):
    return 0 <= position[0] < rows and 0 <= position[1] < columns


rows, columns = [int(x) for x in input().split()]
bunnies_lair = []
player_position = []
bunnies_positions = []

for row in range(rows):
    bunnies_lair.append([x for x in input()])
    for i in range(len(bunnies_lair[row])):
        if bunnies_lair[row][i] == 'B':
            bunnies_positions.append([row, i])
        elif bunnies_lair[row][i] == 'P':
            player_position = [row, i]

commands = deque(input())
directions = {
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1],
    'R': [0, 1]
}

condition = ''

while commands:
    command = commands.popleft()
    new_position = [directions[command][0] + player_position[0], directions[command][1] + player_position[1]]
    bunnies_lair[player_position[0]][player_position[1]] = '.'

    if check_index(new_position):
        if bunnies_lair[new_position[0]][new_position[1]] == 'B':
            condition = 'dead'

        elif bunnies_lair[new_position[0]][new_position[1]] == '.':
            bunnies_lair[new_position[0]][new_position[1]] = 'P'

        player_position = new_position

    else:
        condition = 'won'

    new_bunnies_positions = []
    for bunny in bunnies_positions:
        for i in directions:
            new_bunny = [directions[i][0] + bunny[0], directions[i][1] + bunny[1]]
            if check_index(new_bunny) and new_bunny not in new_bunnies_positions:
                new_bunnies_positions.append(new_bunny)

    for i in new_bunnies_positions:
        if bunnies_lair[i[0]][i[1]] == '.':
            bunnies_lair[i[0]][i[1]] = 'B'
        elif bunnies_lair[i[0]][i[1]] == 'P':
            bunnies_lair[i[0]][i[1]] = 'B'
            condition = 'dead'
    bunnies_positions.extend(new_bunnies_positions)

    if condition:
        break

for r in bunnies_lair:
    print(*r, sep='')
print(f"{condition}: {' '.join(str(x) for x in player_position)}")