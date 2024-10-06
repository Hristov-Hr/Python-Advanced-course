def check_index(x, y):
    if x < 0:
        x = y
    if x > y:
        x = 0
    return x


rows, cols = [int(n) for n in input().split(', ')]
matrix = []
player_position = []
total_gifts = rows * cols - 1

for i in range(rows):
    matrix.append(input().split())
    if 'Y' in matrix[i]:
        player_position = [i, matrix[i].index('Y')]
    total_gifts -= matrix[i].count('.')
matrix[player_position[0]][player_position[1]] = 'x'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

collected_items = {'Christmas decorations': 0, 'Gifts': 0, 'Cookies': 0}

while total_gifts > 0:
    command = input().split('-')
    if command[0] == 'End':
        break

    direction = directions[command[0]]
    steps = int(command[1])

    for _ in range(steps):
        row = check_index(player_position[0] + direction[0], rows - 1)
        col = check_index(player_position[1] + direction[1], cols - 1)
        player_position = [row, col]

        if matrix[row][col] == 'D':
            collected_items['Christmas decorations'] += 1
        elif matrix[row][col] == 'G':
            collected_items['Gifts'] += 1
        elif matrix[row][col] == 'C':
            collected_items['Cookies'] += 1
        if matrix[row][col] in ['D', 'G', 'C']:
            total_gifts -= 1
            if total_gifts == 0:
                break
        matrix[row][col] = 'x'

matrix[player_position[0]][player_position[1]] = 'Y'

if total_gifts == 0:
    print('Merry Christmas!')
print("You've collected:")
[print(f"- {v} {k}") for k, v in collected_items.items()]
[print(*m) for m in matrix]