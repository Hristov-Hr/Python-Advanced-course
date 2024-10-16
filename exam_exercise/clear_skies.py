SIZE = int(input())
airspace = []
fighter_position = []
armor = 300
enemy = 4

for i in range(SIZE):
    airspace.append([x for x in input()])
    if 'J' in airspace[i]:
        fighter_position = [i, airspace[i].index('J')]
        airspace[i][fighter_position[1]] = '-'

mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    direction = input()
    next_row = fighter_position[0] + mapper[direction][0]
    next_col = fighter_position[1] + mapper[direction][1]
    fighter_position = [next_row, next_col]

    if airspace[next_row][next_col] == 'E':
        enemy -= 1
        if enemy == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        armor -= 100
        if armor == 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!")
            break
    if airspace[next_row][next_col] == 'R':
        armor = 300
    airspace[next_row][next_col] = '-'

airspace[fighter_position[0]][fighter_position[1]] = 'J'
[print(''.join(a)) for a in airspace]