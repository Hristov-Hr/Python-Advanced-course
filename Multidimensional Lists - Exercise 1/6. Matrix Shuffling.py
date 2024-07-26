rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command, *data = input().split()
    if command == 'END':
        break
    if command != 'swap' or len(data) != 4:
        print('Invalid input!')
        continue
    row_1, col_1, row_2, col_2 = [int(x) for x in data]
    if 0 <= row_1 < rows and 0 <= row_2 < rows and 0 <= col_1 < columns and 0 <= col_2 < columns:
        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
        for row in matrix:
            print(*row)
    else:
        print('Invalid input!')
        continue