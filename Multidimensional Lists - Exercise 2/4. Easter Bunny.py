field_size = int(input())
field = []
bunny_position = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
max_eggs = float('-inf')
best_direction = ''
best_way = []

for i in range(field_size):
    field.append(input().split())
    if 'B' in field[i]:
        bunny_position = [i, field[i].index('B')]

for k, v in directions.items():
    row, col = bunny_position
    result = 0
    direction = []
    while True:
        row += v[0]
        col += v[1]
        if not 0 <= row < field_size or not 0 <= col < field_size:
            break
        if field[row][col] == "X":
            break
        direction.append([row, col])
        result += int(field[row][col])
    if not direction:
        result = float('-inf')
    if result > max_eggs:
        max_eggs = result
        best_direction = k
        best_way = direction

print(best_direction)
print(*best_way, sep='\n')
print(max_eggs)