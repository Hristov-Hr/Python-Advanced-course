matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    matrix.append([x for x in input()])

symbol = input()
found_index = ()

for i in range(matrix_size):
    for j in range(matrix_size):
        if matrix[i][j] == symbol:
            found_index = (i, j)
            break
    if found_index:
        print(found_index)
        break
else:
    print(f"{symbol} does not occur in the matrix")