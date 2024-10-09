SIZE = int(input())
battlefield = []
row, col = 0, 0
cruisers = 3
hit_points = 3

for i in range(SIZE):
    battlefield.append([x for x in input()])
    if 'S' in battlefield[i]:
        row, col = i, battlefield[i].index('S')
        battlefield[row][col] = '-'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

while cruisers > 0 and hit_points > 0:
    r, c = directions[input()]
    row += r
    col += c

    if battlefield[row][col] == '*':
        hit_points -= 1
    elif battlefield[row][col] == 'C':
        cruisers -= 1
    battlefield[row][col] = '-'
battlefield[row][col] = 'S'

print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!") if not cruisers else \
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
[print(''.join(b)) for b in battlefield]