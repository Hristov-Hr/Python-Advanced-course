table = [input().split() for _ in range(6)]
row, col = [int(n.strip('()')) for n in input().split(', ')]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


command = input()

while command != 'Stop':
    operation, direction, *value = command.split(', ')
    r, c = directions[direction]
    row += r
    col += c

    if operation == 'Create':
        table[row][col] = value[0] if table[row][col] == '.' else table[row][col]

    elif operation == 'Update':
        table[row][col] = value[0] if table[row][col] != '.' else '.'

    elif operation == 'Delete':
        table[row][col] = '.'

    elif operation == 'Read' and table[row][col].isalnum():
        print(table[row][col])

    command = input()

[print(*t) for t in table]