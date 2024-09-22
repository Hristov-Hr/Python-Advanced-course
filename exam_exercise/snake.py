SIZE = int(input())
matrix = []
snake_position = []

for i in range(SIZE):
    row = [x for x in input()]
    matrix.append(row)
    if 'S' in row:
        snake_position = [i, matrix[i].index('S')]
        matrix[i][snake_position[1]] = '.'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

eaten_food = 0

while eaten_food < 10:

    row, col = directions[input()]
    row += snake_position[0]
    col += snake_position[1]

    if row < 0 or row >= SIZE or col < 0 or col >= SIZE:
        break

    if matrix[row][col] == '*':
        eaten_food += 1

    elif matrix[row][col] == 'B':
        matrix[row][col] = '.'

        for i in range(len(matrix)):
            if 'B' in matrix[i]:
                row = i
                col = matrix[i].index('B')

    matrix[row][col] = '.'
    snake_position = [row, col]

else:
    matrix[snake_position[0]][snake_position[1]] = 'S'

print('You won! You fed the snake.') if eaten_food == 10 else print('Game over!')
print(f"Food eaten: {eaten_food}")
[print(*r, sep='') for r in matrix]