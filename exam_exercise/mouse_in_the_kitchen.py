def is_valid_idx(r, c):
    return 0 <= r < rows and 0 <= c < cols


rows, cols = [int(n) for n in input().split(',')]
matrix = []
mouse_position = []
cheeses = 0

for i in range(rows):
    matrix.append([x for x in input()])
    if 'M' in matrix[i]:
        mouse_position = [i, matrix[i].index('M')]
        matrix[i][mouse_position[1]] = '*'
    if 'C' in matrix[i]:
        cheeses += matrix[i].count('C')

mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

command = input()

while command != "danger":
    row, col = mouse_position[0] + mapper[command][0], mouse_position[1] + mapper[command][1]

    if not is_valid_idx(row, col):
        print("No more cheese for tonight!")
        break

    elif matrix[row][col] == '@':
        command = input()
        continue

    mouse_position = [row, col]

    if matrix[row][col] == 'C':
        matrix[row][col] = '*'
        cheeses -= 1
        if cheeses == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix[row][col] == 'T':
        print("Mouse is trapped!")
        break
    command = input()

else:
    print("Mouse will come back later!")

matrix[mouse_position[0]][mouse_position[1]] = 'M'

[print(''.join(m)) for m in matrix]