size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

command = input()

while command != 'END':
    command_, row_index, col_index, value = command.split()
    if 0 <= int(row_index) < size and 0 <= int(col_index) < len(matrix[0]):
        if command_ == 'Add':
            matrix[int(row_index)][int(col_index)] += int(value)
        elif command_ == 'Subtract':
            matrix[int(row_index)][int(col_index)] -= int(value)
    else:
        print('Invalid coordinates')
    command = input()

[print(*r) for r in matrix]