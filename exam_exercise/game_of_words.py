def is_valid_idx(r, c):
    return 0 <= r < size and 0 <= c < size


text = input()
size = int(input())
field = []
player_position = []

for i in range(size):
    field.append(list(input()))

    if 'P' in field[i]:
        player_position = i, field[i].index('P')
        field[i][player_position[1]] = '-'


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for _ in range(int(input())):

    row, col = directions[input()]
    row += player_position[0]
    col += player_position[1]

    if not is_valid_idx(row, col):
        text = text[:-1]
        continue

    if field[row][col].isalpha():
        text += field[row][col]
        field[row][col] = '-'
    player_position = row, col

field[player_position[0]][player_position[1]] = 'P'

if text:
    print(text)
[print(*mtr, sep='') for mtr in field]