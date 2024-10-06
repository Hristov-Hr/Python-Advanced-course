def is_valid_index(r, c):
    return 0 <= r < 8 and 0 <= c < 8


def check_for_capture(r, c):
    is_winner = False
    for j in [-1, 1]:
        if is_valid_index(r, c + j) and matrix[r][c + j] != '-':
            is_winner = True
    return is_winner


matrix = []
white_position = []
black_position = []

for i in range(8):
    matrix.append(input().split())
    if 'b' in matrix[i]:
        black_position = [i, matrix[i].index('b')]
    if 'w' in matrix[i]:
        white_position = [i, matrix[i].index('w')]

winner = ''

while True:
    w_row, w_col = white_position
    b_row, b_col = black_position

    if check_for_capture(w_row - 1, w_col):
        winner = f"Game over! White win, capture on {chr(97 + b_col)}{8 - b_row}."
        break
    matrix[w_row][w_col] = '-'
    w_row -= 1
    matrix[w_row][w_col] = 'w'
    white_position = [w_row, w_col]
    if w_row == 0:
        winner = f"Game over! White pawn is promoted to a queen at {chr(97 + w_col)}8."
        break

    if check_for_capture(b_row + 1, b_col):
        winner = f"Game over! Black win, capture on {chr(97 + w_col)}{8 - w_row}."
        break
    matrix[b_row][b_col] = '-'
    b_row += 1
    matrix[b_row][b_col] = 'b'
    black_position = [b_row, b_col]
    if b_row == 7:
        winner = f"Game over! Black pawn is promoted to a queen at {chr(97 + b_col)}1."
        break

print(winner)