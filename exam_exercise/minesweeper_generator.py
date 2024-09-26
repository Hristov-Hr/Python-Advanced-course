def is_valid_index(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE


SIZE = int(input())

matrix = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

for _ in range(int(input())):

    bomb = input().strip('()')
    row, col = [int(n) for n in bomb.split(', ')]
    matrix[row][col] = '*'

    for d in directions:
        row_pos = row + d[0]
        col_pos = col + d[1]
        if not is_valid_index(row_pos, col_pos) or matrix[row_pos][col_pos] == '*':
            continue
        matrix[row_pos][col_pos] += 1

[print(*m) for m in matrix]

