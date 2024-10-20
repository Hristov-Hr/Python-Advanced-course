def field_boundaries(r, c):
    return 0 <= r < rows and 0 <= c < cols


rows, cols = [int(n) for n in input().split(', ')]
matrix = []
start_position = []
bomb_position = []

for i in range(rows):
    matrix.append([x for x in input()])
    if 'C' in matrix[i]:
        start_position = [i, matrix[i].index('C')]
    if 'B' in matrix[i]:
        bomb_position = [i, matrix[i].index('B')]

mapper = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

time = 16
sapper_position = start_position.copy()

while time > 0:
    time -= 1
    command = input()
    if command != 'defuse':
        next_row = sapper_position[0] + mapper[command][0]
        next_col = sapper_position[1] + mapper[command][1]
        if not field_boundaries(next_row, next_col):
            continue
        sapper_position = [next_row, next_col]

        if matrix[next_row][next_col] == 'T':
            matrix[next_row][next_col] = '*'
            print("Terrorists win!")
            is_killed = True
            break

    else:
        if sapper_position[0] != bomb_position[0] or sapper_position[1] != bomb_position[1]:
            time -= 1
            continue
        time -= 3
        if time >= 0:
            matrix[bomb_position[0]][bomb_position[1]] = "D"
            print("Counter-terrorist wins!")
            print(f"Bomb has been defused: {time} second/s remaining.")
            break
        matrix[bomb_position[0]][bomb_position[1]] = "X"

else:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {abs(time)} second/s.")

[print(''.join(m)) for m in matrix]

