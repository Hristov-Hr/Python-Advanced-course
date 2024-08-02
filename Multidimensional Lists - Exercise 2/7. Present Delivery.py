def move(position, direction):
    r = position[0] + direction[0]
    c = position[1] + direction[1]
    if 0 <= r < size and 0 <= c < size:
        return [r, c]
    return position


def nice_kid(present, happy_kid):
    return present - 1, happy_kid + 1


def cookie(position, present, happy_kid):
    for k, v in directions.items():
        r = position[0] + v[0]
        c = position[1] + v[1]
        if neighborhood[r][c] == 'V':
            present, happy_kid = nice_kid(present, happy_kid)
        elif neighborhood[r][c] == 'X':
            present -= 1
        neighborhood[r][c] = '-'

    return present, happy_kid


presents = int(input())
size = int(input())
neighborhood = []
santa_position = []
nice_kids = 0
happy_nice_kids = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for i in range(size):
    neighborhood.append(input().split())
    nice_kids += neighborhood[i].count('V')
    if 'S' in neighborhood[i]:
        santa_position = [i, neighborhood[i].index('S')]
        neighborhood[i][santa_position[1]] = '-'

while presents > 0:
    command = input()

    if command == 'Christmas morning':
        break

    santa_position = move(santa_position, directions[command])
    row, col = santa_position

    if neighborhood[row][col] == 'V':
        presents, happy_nice_kids = nice_kid(presents, happy_nice_kids)

    elif neighborhood[row][col] == 'C':
        presents, happy_nice_kids = cookie(santa_position, presents, happy_nice_kids)

    neighborhood[row][col] = '-'
    if happy_nice_kids == nice_kids:
        break

else:
    print('Santa ran out of presents!')

neighborhood[santa_position[0]][santa_position[1]] = 'S'
[print(*x) for x in neighborhood]
print(f"Good job, Santa! {nice_kids} happy nice kid/s.") if nice_kids == happy_nice_kids else \
    print(f"No presents for {nice_kids - happy_nice_kids} nice kid/s.")