def field_boundary(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE


SIZE = int(input())
field = []
player_position = []
health = 100

for i in range(SIZE):
    field.append([x for x in input()])
    if 'P' in field[i]:
        player_position = [i, field[i].index('P')]
        field[i][player_position[1]] = '-'

mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    next_row = player_position[0] + mapper[command][0]
    next_col = player_position[1] + mapper[command][1]
    if not field_boundary(next_row, next_col):
        continue
    player_position = [next_row, next_col]

    if field[next_row][next_col] == "X":
        print("Player escaped the maze. Danger passed!")
        break

    elif field[next_row][next_col] == "H":
        health += 15
        if health > 100:
            health = 100

    elif field[next_row][next_col] == "M":
        health -= 40
        if health <= 0:
            health = 0
            print("Player is dead. Maze over!")
            break

    field[next_row][next_col] = "-"

field[player_position[0]][player_position[1]] = "P"
print(f"Player's health: {health} units")
[print(''.join(f)) for f in field]
