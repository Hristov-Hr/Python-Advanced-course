def is_valid_idx(r, c):
    return 0 <= r < rows and 0 <= c < cols


rows, cols = [int(n) for n in input().split(' ')]
start_position = []
neighbor_hood = []

for i in range(rows):
    neighbor_hood.append([x for x in input()])
    if 'B' in neighbor_hood[i]:
        start_position = [i, neighbor_hood[i].index('B')]

mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

boy_position = start_position.copy()
is_successful_delivery = False

while True:
    row, col = mapper[input()]
    row += boy_position[0]
    col += boy_position[1]

    if not is_valid_idx(row, col):
        print("The delivery is late. Order is canceled.")
        break
    elif neighbor_hood[row][col] == '*':
        continue
    else:
        boy_position = [row, col]

    if neighbor_hood[row][col] == 'P':
        print("Pizza is collected. 10 minutes for delivery.")
        neighbor_hood[boy_position[0]][boy_position[1]] = 'R'

    elif neighbor_hood[row][col] == 'A':
        print("Pizza is delivered on time! Next order...")
        neighbor_hood[boy_position[0]][boy_position[1]] = 'P'
        is_successful_delivery = True
        break
    else:
        neighbor_hood[boy_position[0]][boy_position[1]] = '.'

if is_successful_delivery:
    neighbor_hood[start_position[0]][start_position[1]] = 'B'
else:
    neighbor_hood[start_position[0]][start_position[1]] = ' '

[print(''.join(n)) for n in neighbor_hood]

