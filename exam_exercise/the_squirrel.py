from collections import deque


def is_valid_index(r, c, s):
    return 0 <= r < s and 0 <= c < s


SIZE = int(input())
directions = deque(input().split(', '))
field = []
squirrel_position = []
hazelnuts = 0

for i in range(SIZE):
    field.append([x for x in input()])
    if 's' in field[i]:
        squirrel_position = [i, field[i].index('s')]
        field[i][squirrel_position[1]] = '*'

mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while hazelnuts < 3 and directions:

    direction = directions.popleft()
    row, col = squirrel_position[0] + mapper[direction][0], squirrel_position[1] + mapper[direction][1]
    squirrel_position = [row, col]

    if not is_valid_index(row, col, SIZE):
        print("The squirrel is out of the field.")
        break

    elif field[row][col] == 'h':
        hazelnuts += 1
        field[row][col] = "*"

    elif field[row][col] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        break

else:
    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
    else:
        print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")