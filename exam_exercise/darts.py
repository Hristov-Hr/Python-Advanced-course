from collections import deque


def calculate_points(r, c):
    return int(matrix[0][c]) + int(matrix[6][c]) + int(matrix[r][0]) + int(matrix[r][6])


def valid_index(r, c):
    return 0 <= r < 7 and 0 <= c < 7


players = deque(input().split(', '))
points = dict.fromkeys(players, 501)
matrix = [input().split() for _ in range(7)]
winner = ''
counter = 1

while True:
    player = players[0]
    command = input().strip('()')
    row, col = [int(n) for n in command.split(', ')]
    current_points = 0
    counter += 1

    targets = {
        'D': lambda x, y: calculate_points(x, y) * 2,
        'T': lambda x, y: calculate_points(x, y) * 3,
        'B': lambda x, y: 501
    }

    if not valid_index(row, col):
        current_points = 0

    elif matrix[row][col].isdigit():
        current_points += int(matrix[row][col])

    else:
        current_points += targets[matrix[row][col]](row, col)

    points[player] -= current_points

    if points[player] <= 0:
        winner = player
        break

    players.rotate(1)

print(f"{winner} won the game with {counter // 2} throws!")
