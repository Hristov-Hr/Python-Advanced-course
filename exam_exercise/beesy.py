def move(j):
    if j < 0:
        return SIZE - 1
    if j >= SIZE:
        return 0
    return j


SIZE = int(input())
field = []
bee_position = []
energy = 15
collected_nectar = 0
is_restored = False

for i in range(SIZE):
    field.append([x for x in input()])
    if 'B' in field[i]:
        bee_position = [i, field[i].index('B')]
        field[i][bee_position[1]] = '-'

mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while energy > 0:
    energy -= 1
    command = input()
    next_row = move(bee_position[0] + mapper[command][0])
    next_col = move(bee_position[1] + mapper[command][1])
    bee_position = [next_row, next_col]

    if field[next_row][next_col] == "H":
        print(f"Great job, Beesy! The hive is full. Energy left: {energy}") if collected_nectar >= 30 else \
            print("Beesy did not manage to collect enough nectar.")
        break
    if field[next_row][next_col].isdigit():
        collected_nectar += int(field[next_row][next_col])
        field[next_row][next_col] = "-"
    if energy == 0 and collected_nectar >= 30 and is_restored is False:
        is_restored = True
        energy += collected_nectar - 30
        collected_nectar = 30
else:
    print("This is the end! Beesy ran out of energy.")

field[bee_position[0]][bee_position[1]] = 'B'

[print(''.join(f)) for f in field]