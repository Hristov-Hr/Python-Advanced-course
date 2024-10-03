from math import floor


def new_position(position, move):
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    r, c = directions[move]
    r += position[0]
    c += position[1]
    r = check_index(r)
    c = check_index(c)

    return r, c


def check_index(x):
    if x < 0:
        x = SIZE - 1
    elif x >= SIZE:
        x = 0
    else:
        pass
    return x


SIZE = int(input())
matrix = []
player_position = []

for i in range(SIZE):
    matrix.append(input().split())
    if "P" in matrix[i]:
        player_position.append([i, matrix[i].index('P')])
matrix[player_position[0][0]][player_position[0][1]] = 0

coins = 0

while coins < 100:
    row, col = new_position(player_position[-1], input())
    player_position.append([row, col])
    if matrix[row][col] == 'X':
        break
    coins += int(matrix[row][col])
    matrix[row][col] = 0

print(f"You won! You've collected {coins} coins.") if coins >= 100 else \
    print(f"Game over! You've collected {floor(coins / 2)} coins.")
print("Your path:")
print(*player_position, sep='\n')