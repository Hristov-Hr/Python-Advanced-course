def movement(pos, move):
    mapper = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    r, c = mapper[move]
    r += pos[0]
    c += pos[1]
    if r < 0:
        r = SIZE - 1
    elif r > SIZE - 1:
        r = 0
    if c < 0:
        c = SIZE - 1
    elif c > SIZE - 1:
        c = 0
    return r, c


SIZE = int(input())
matrix = []
position = []

for i in range(SIZE):
    matrix.append([x for x in input()])
    if 'S' in matrix[i]:
        position = [i, matrix[i].index('S')]
        matrix[i][position[1]] = '-'

fish = 0
is_sank = False
command = input()

while command != 'collect the nets':
    row, col = movement(position, command)
    position = [row, col]

    if matrix[row][col] == 'W':
        is_sank = True
        break

    elif matrix[row][col].isdigit():
        fish += int(matrix[row][col])
        matrix[row][col] = '-'

    command = input()

matrix[position[0]][position[1]] = 'S'
if is_sank:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{position[0]},{position[1]}]")
else:
    if fish >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish} tons of fish more.")
    print(f"Amount of fish caught: {fish} tons.") if fish > 0 else None
    [print(''.join(m)) for m in matrix]
