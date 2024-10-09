SIZE = int(input())
tracked_car = input()
race_route = [input().split() for _ in range(SIZE)]
row, col = 0, 0
distance = 0
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}
is_finished = False

command = input()
while command != 'End':
    r, c = directions[command]
    row += r
    col += c
    distance += 10

    if race_route[row][col] == 'T':
        distance += 20
        race_route[row][col] = '.'
        for i in range(len(race_route)):
            if 'T' in race_route[i]:
                row, col = i, race_route[i].index('T')
                race_route[row][col] = '.'

    elif race_route[row][col] == 'F':
        is_finished = True
        break

    command = input()

race_route[row][col] = 'C'

print(f"Racing car {tracked_car} finished the stage!" if is_finished else f"Racing car {tracked_car} DNF.")
print(f"Distance covered {distance} km.")
[print(''.join(r)) for r in race_route]