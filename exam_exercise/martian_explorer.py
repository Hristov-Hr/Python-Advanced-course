from collections import deque


def check_index(r, c):
    r = 5 if r < 0 else r
    r = 0 if r > 5 else r
    c = 5 if c < 0 else c
    c = 0 if c > 5 else c
    return r, c


matrix = []
rover_position = []

for i in range(6):
    matrix.append(input().split())
    if 'E' in matrix[i]:
        rover_position = [i, matrix[i].index('E')]
        matrix[i][rover_position[1]] = '-'

commands = deque(input().split(', '))
movements = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

found_deposits = set()

while commands:
    direction = movements[commands.popleft()]
    row, col = check_index(direction[0] + rover_position[0], direction[1] + rover_position[1])
    rover_position = [row, col]
    if matrix[row][col] == 'W':
        print(f"Water deposit found at ({row}, {col})")
        found_deposits.add('W')
    elif matrix[row][col] == 'M':
        print(f"Metal deposit found at ({row}, {col})")
        found_deposits.add('M')
    elif matrix[row][col] == 'C':
        print(f"Concrete deposit found at ({row}, {col})")
        found_deposits.add('C')
    elif matrix[row][col] == 'R':
        print(f"Rover got broken at ({row}, {col})")
        break

print("Area suitable to start the colony.") if len(found_deposits) == 3 else \
    print("Area not suitable to start the colony.")



