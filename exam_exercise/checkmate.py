def valid_position(c, r):
    return 0 <= c < 8 and 0 <= r < 8


board = []
king_position = []

for i in range(8):
    board.append(input().split())
    if 'K' in board[i]:
        king_position = [i, board[i].index('K')]

directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
queens = []

for d in directions:
    row, col = king_position
    while valid_position(row, col):
        if board[row][col] == 'Q':
            queens.append([row, col])
            break
        row += d[0]
        col += d[1]

print(*queens, sep='\n') if queens else print('The king is safe!')