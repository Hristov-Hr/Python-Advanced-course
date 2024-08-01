def check_knights_positions(r, c):
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    counter = 0
    for direction in directions:
        r_ = r + direction[0]
        c_ = c + direction[1]
        if valid_index(r_, c_) and board[r_][c_] == 'K':
            counter += 1
    return counter


def valid_index(ro, co):
    return 0 <= ro < size and 0 <= co < size


size = int(input())
board = []
knights_positions = {}
removed_knights = 0

for i in range(size):
    board.append([x for x in input()])
    for j in range(size):
        if board[i][j] == 'K':
            knights_positions[(i, j)] = 0

while True:
    for key, value in knights_positions.items():
        row, col = key
        knights_positions[key] = check_knights_positions(row, col)

    sorted_knights = sorted(knights_positions.items(), key=lambda x: x[1], reverse=True)

    if sorted_knights[0][1] > 0:
        knights_positions.pop(sorted_knights[0][0])
        removed_knights += 1
        board[sorted_knights[0][0][0]][sorted_knights[0][0][1]] = '0'
    else:
        break

print(removed_knights)