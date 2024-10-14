def check_idx(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE


SIZE = int(input())
field = []
player_position = []
amount = 100

for i in range(SIZE):
    field.append([x for x in input()])
    if 'G' in field[i]:
        player_position = [i, field[i].index('G')]
        field[i][player_position[1]] = '-'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

command = input()

while amount > 0 and command != 'end':
    next_row = player_position[0] + directions[command][0]
    next_col = player_position[1] + directions[command][1]
    player_position = [next_row, next_col]

    if not check_idx(next_row, next_col):
        amount = 0
        break

    elif field[next_row][next_col] == 'W':
        amount += 100

    elif field[next_row][next_col] == 'P':
        amount -= 200

    elif field[next_row][next_col] == 'J':
        amount += 100000
        print("You win the Jackpot!")
        break

    field[next_row][next_col] = '-'
    command = input()

field[player_position[0]][player_position[1]] = 'G'

if amount > 0:
    print(f"End of the game. Total amount: {amount}$")
    [print(''.join(f)) for f in field]
else:
    print("Game over! You lost everything!")