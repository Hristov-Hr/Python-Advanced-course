def init_matrix():
    matrix = []
    position = []

    for i in range(size):
        row = input().split()
        if 'P' in row:
            position = [i, row.index("P")]
            row[row.index("P")] = "."
        matrix.append(row)

    return matrix, position


def check_index(row, col):
    return 0 <= row < size and 0 <= col < size


size = int(input())
stars = 2
field, player_position = init_matrix()


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while 0 < stars < 10:
    command = input()

    r, c = directions[command][0] + player_position[0], directions[command][1] + player_position[1]

    if not check_index(r, c):
        r, c = 0, 0

    if field[r][c] == "#":
        stars -= 1
        continue

    elif field[r][c] == "*":
        stars += 1
        field[r][c] = "."

    player_position = [r, c]

field[player_position[0]][player_position[1]] = "P"
print("You won! You have collected 10 stars." if stars == 10 else "Game over! You are out of any stars.")
print(f"Your final position is {player_position}")
[print(' '.join(r)) for r in field]