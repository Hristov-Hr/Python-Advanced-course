def is_index_in_field(r, c):
    return 0 <= r < rows and 0 <= c < cols


rows, cols = [int(n) for n in input().split()]
matrix = []
player_position = []

for i in range(rows):
    matrix.append(input().split())
    if 'B' in matrix[i]:
        player_position = [i, matrix[i].index('B')]
        matrix[i][player_position[1]] = '-'


directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)
              }

touched_opponents = 0
total_moves = 0

while touched_opponents < 3:
    command = input()
    if command == 'Finish':
        break

    row, col = directions[command]
    row += player_position[0]
    col += player_position[1]

    if not is_index_in_field(row, col) or matrix[row][col] == 'O':
        continue
    elif matrix[row][col] == 'P':
        touched_opponents += 1
    total_moves += 1
    player_position = [row, col]

print('Game over!')
print(f"Touched opponents: {touched_opponents} Moves made: {total_moves}")